import json
import pandas as pd
import cx_Oracle
import asyncio
import websockets
import aioconsole
from 위경도좌표변환 import mapToGrid
from 단기예보 import get_request_url;
from 전처리 import json_to_df_info,websocket_rains;
from 오라클 import preprocessed_df_to_oracle,select_from_oracle,new_oracle,preprocessed_df_to_oracle2,select_from_oracle2;
import atexit

# rains_dict = []
# rains_dict = websocket_rains(select_from_oracle()).to_dict(orient='records')
# print(rains_dict)


connected = set()  # 연결된 클라이언트를 추적하기 위한 집합
global_varible = 0
global_x = 0
global_y = 0
async def handle(websocket, path): # websocket 는 연결 객체 path는 클라이언트가 요청한 웹소켓 url경로
    global global_varible
    global global_x
    global global_y
    connected.add(websocket)  # 클라이언트 연결을 집합에 추가
    print(len(connected)) # 처음엔 1 html 새로고침시 1씩 증가하네요
    print("서버 구동 중")
    data= await websocket.recv()
    if global_varible == 0:
        print("한번만")
        latitude,longitude = data.split(',')
        latitude = float(latitude)
        longitude = float(longitude)
        x,y = mapToGrid(latitude, longitude)
        get_request_url(x,y)
        preprocessed_df_to_oracle2(json_to_df_info(get_request_url(x,y)))
        global_x = x[0]
        global_y = y[0]
        global_varible += 1
    print("오라클실행")
    df = select_from_oracle2(global_x,global_y)
    df['baseDate'] = df['baseDate'].astype(str)
    df['fcstDate'] = df['fcstDate'].astype(str)
    rains_dict = df.to_dict(orient='records')
    print(rains_dict)
    try:
        rains_json = json.dumps(rains_dict)
        for client in connected:
            try:
                await client.send(rains_json)
            except websockets.exceptions.ConnectionClosed:
                print("Client 접속 해제")
    finally:
        if websocket in connected:
            connected.remove(websocket)
def handle_exit():
    new_oracle()


atexit.register(handle_exit)

print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060) # 웹소켓 서버 객체 생성 handle 는 연결될 때 실행되는 함수
asyncio.get_event_loop().run_until_complete(start_server) # 완료 될 때 까지 함수 실행
asyncio.get_event_loop().run_forever() # 이벤트 루프를 시작하고 무한정 실행하는데 사용
