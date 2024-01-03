import asyncio
import websockets
import json
import aioconsole
import random

async def handle(websocket, path):
    print("서버 구동 중")
    try:
        while True:
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")
            if user_input == '1':
                while True:
                    price = random.randint(100, 200)  # 임의의 가격 생성
                    data = {"company": "삼성전자", "price": price}
                    json_data = json.dumps(data)  # 데이터를 JSON 형식으로 직렬화
                    await websocket.send(json_data)  # 클라이언트로 데이터 전송
                    await asyncio.sleep(1)
    except websockets.exceptions.ConnectionClosed:
        print("Client 접속 해제")

print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
