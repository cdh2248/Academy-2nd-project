import asyncio
import websockets
import aioconsole
import json
import random

connected = set()  # 연결된 클라이언트를 추적하기 위한 집합


async def handle(websocket, path):
    connected.add(websocket)  # 클라이언트 연결을 집합에 추가
    print("서버 구동 중")

    try:
        while True:
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")

            if user_input == '1':
                initial_data = [
                    {"company": "삼성전자", "price": 73000},
                    {"company": "LG에너지솔루션", "price": 518000},
                    {"company": "SK하이닉스", "price": 116700}
                ]

                json_data = json.dumps(initial_data)  # 초기 데이터를 JSON 형식으로 직렬화
                for client in connected:
                    try:
                        await client.send(json_data)
                    except websockets.exceptions.ConnectionClosed:
                        print("Client 접속 해제")

                    while True:
                        # 최대 10% 범위 내에서 랜덤하게 상승 또는 하락
                        for data in initial_data:
                            change_percent = random.uniform(-0.1, 0.1)
                            data["price"] += int(data["price"] * change_percent)

                        json_data = json.dumps(initial_data)
                        for client in connected:
                            try:
                                await client.send(json_data)
                                await asyncio.sleep(2)  # 2초 대기
                            except websockets.exceptions.ConnectionClosed:
                                print("Client 접속 해제")


    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거


print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
