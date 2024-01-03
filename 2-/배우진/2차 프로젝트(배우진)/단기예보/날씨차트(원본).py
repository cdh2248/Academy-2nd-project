import asyncio
import websockets
import aioconsole
import json
import random

connected = set()  # 연결된 클라이언트를 추적하기 위한 집합


async def handle(websocket, path): # websocket 는 연결 객체 path는 클라이언트가 요청한 웹소켓 url경로
    connected.add(websocket)  # 클라이언트 연결을 집합에 추가
    print(len(connected)) # 처음엔 1 html 새로고침시 1씩 증가하네요
    print("서버 구동 중")

    try:
        while True:
            # 비동기 방식으로 사용자의 입력을 기다리고 입력된 값을 반환
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")

            if user_input == '1':
                initial_data = [
                    {"company": "삼성전자", "price": 73000},
                    {"company": "LG에너지솔루션", "price": 518000},
                    {"company": "SK하이닉스", "price": 116700}
                ]
                # print(type(initial_data)) # 리스트 타입 안에 딕트 타입이 있음
                # 초기 데이터를 JSON 형식으로 직렬화
                # 데이터를 텍스트 형식으로 표현 send 메서드에 문자열 형태로 데이터를 제공해야 하기 때문
                json_data = json.dumps(initial_data)
                # print(type(json_data)) # str 타입
                # print(json_data)
                for client in connected:
                    try:
                        await client.send(json_data) # 데이터를 서버로 전송하고 응답을 기다림
                    except websockets.exceptions.ConnectionClosed: # 웹소켓이 닫혔을 때 실행
                        print("Client 접속 해제")

                    while True: # 2마다 통신 서버에 데이터 전송
                        # 최대 10% 범위 내에서 랜덤하게 상승 또는 하락
                        for data in initial_data:
                            change_percent = random.uniform(-0.1, 0.1)
                            data["price"] += int(data["price"] * change_percent)

                        json_data = json.dumps(initial_data)
                        for client in connected:
                            try:
                                await client.send(json_data)
                                await asyncio.sleep(0.5)  # 2초 대기
                            except websockets.exceptions.ConnectionClosed:
                                print("Client 접속 해제")


    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거


print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060) # 웹소켓 서버 객체 생성 handle 는 연결될 때 실행되는 함수
asyncio.get_event_loop().run_until_complete(start_server) # 완료 될 때 까지 함수 실행
asyncio.get_event_loop().run_forever() # 이벤트 루프를 시작하고 무한정 실행하는데 사용
