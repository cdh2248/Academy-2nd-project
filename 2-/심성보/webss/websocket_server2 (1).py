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
            # 일반 input함수를 사용하면 비동기 처리가 되지 않는다.
            # 소켓 통신 프로그램 수행시 콘솔 input은 아래 함수를 사용한다.
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")

            if user_input == '1':
                data = [
                    {"name": "김유신", "korean": 90, "english": 85, "math": 95},
                    {"name": "이문세", "korean": 80, "english": 90, "math": 88},
                    {"name": "장지원", "korean": 95, "english": 92, "math": 87}
                ]

                # 모든 연결된 클라이언트에게 데이터 전송
                for client in connected:
                    await client.send(json.dumps(data))
                    # await client.send(str(data))

    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거


print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
