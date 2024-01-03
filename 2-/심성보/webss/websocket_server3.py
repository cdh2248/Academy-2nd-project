import asyncio
import websockets
import aioconsole
import json

connected = set()  # 연결된 클라이언트를 추적하기 위한 집합


async def handle(websocket, path):
    connected.add(websocket)  # 클라이언트 연결을 집합에 추가
    print("서버 구동 중")

    try:
        while True:
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")

            if user_input == '1':
                data = [
                    {"category": "의류", "sales": 1000},
                    {"category": "전자제품", "sales": 2000},
                    {"category": "가구", "sales": 1500},
                    {"category": "식품", "sales": 3000}
                ]

                json_data = json.dumps(data)  # 데이터를 JSON 형식으로 직렬화
                for client in connected:
                    try:
                        await client.send(json_data)
                    except websockets.exceptions.ConnectionClosed:
                        print("Client 접속 해제")

    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거


print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
