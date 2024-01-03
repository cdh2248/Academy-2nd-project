import asyncio
import websockets
import aioconsole
import json

connected = set()  # 연결된 클라이언트를 추적하기 위한 집합

"""
async는 비동기 함수(Asynchronous function)를 정의하기 위한 키워드
비동기 함수는 비동기적인 동작을 수행할 수 있는 함수로, 
await 키워드를 사용하여 비동기 작업의 완료를 기다린다.

async 키워드를 함수 선언 앞에 붙이면 일반적인 동기 함수와는 달리, 
작업이 완료될 때까지 기다리지 않고 다른 작업을 수행할 수 있습니다. 
이를 통해 여러 작업을 동시에 실행하거나, 
I/O 작업과 같이 시간이 걸리는 작업을 효율적으로 처리할 수 있습니다.
"""
async def handle(websocket, path):
    connected.add(websocket)  # 클라이언트 연결을 집합에 추가
    print("서버 구동 중")

    try:
        while True:
            # 일반 input함수를 사용하면 비동기 처리가 되지 않는다.
            # 소켓 통신 프로그램 수행시 콘솔 input은 아래 함수를 사용한다.
            # Multi-Client를 지원해야 하기 때문에 input() 동기함수는 사용할 수 없다.
            # 사용자 입력을 비동기로 받기위해서 비동기함수인 aioconsole.ainput를 사용해야하며
            # 비동기 입력함수의 입력을 기다려야 하기 때문에 await 키워드를 사용해야한다.
            user_input = await aioconsole.ainput("1을 눌러 클라이언트에 데이터를 전송하세요: ")

            if user_input == '1':
                # 데이터 리스트 생성
                data = [
                    {"name": "김유신", "korean": 90, "english": 85, "math": 95},
                    {"name": "이문세", "korean": 80, "english": 90, "math": 88},
                    {"name": "장지원", "korean": 95, "english": 92, "math": 87}
                ]

                # 모든 연결된 클라이언트에게 데이터 전송
                for client in connected:
                    # 데이터를 JSON 형식으로 직렬화하여 클라이언트에게 전송
                    try:
                        await client.send(json.dumps(data))
                    # Client 접속 해제 일 경우 예외처리
                    except websockets.exceptions.ConnectionClosed:
                        print("Client 접속 해제")

    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거


print("서버 구동 시작")
# WebSocket 서버 시작
# serve함수는 SebSocket 서버를 설정하여 클라이언트의 연결을 수신 대기함
# 클라이언트가 서버에 연결되면 handle함수가 각 클라이언트 연결에 대해 호출됨
# 참고] 특정 포트 사용중인지 확인하는 커맨드
# netstat -ano | findstr :8060
start_server = websockets.serve(handle, 'localhost', 8060)

"""
* 멀티쓰레드(Multi-Thread) 방식 프로그래밍에서의 비동기(Asynchronous) 작업
 참고]
 - 동기(Synchronous) 작업: 한 작업이 완료될 때까지 다른 작업을 수행하지 않고 기다리는 작업 
  (예: 번호표를 나누어주고 순서대로 작업을 처리 주문 처리)
 - 비동기(Asynchronous) 작업: 동시에 여러 작업을 수행하는 작업
  (예: 네트워크 프로그램, 이벤트 프로그램, 웹 스크래핑)
"""
# 비동기 이벤트 루프 실행 (비동기 작업을 관리하고 실행하는 데 사용)
asyncio.get_event_loop().run_until_complete(start_server)
# 클라이언트의 연결을 지속적으로 처리하고 서버를 계속해서 실행
asyncio.get_event_loop().run_forever()
