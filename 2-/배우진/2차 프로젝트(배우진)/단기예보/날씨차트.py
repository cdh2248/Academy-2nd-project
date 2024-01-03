import asyncio
import websockets
import aioconsole
import json
import random

import requests
import json
from datetime import datetime, timedelta
import pandas as pd
import cx_Oracle
from flask import Flask, request
from flask_restful import Resource, Api
from flask import Response
import asyncio
import websockets
import aioconsole
import math
from 단기예보 import get_update_time_info
from 단기예보 import get_request_url
from 단기예보 import json_to_df_info
from 단기예보 import category_df
from 단기예보 import preprocessed_df_to_oracle

# ------------------------------------------------------------------------------------------------
def search(word,x):
    a=str(x)
    rs=a.find(word)
    if rs == -1:
        return False
    else:
        return True

def select_from_oracle():
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()
    sql_select = '''
            select * from rains
             '''
    rs = cur.execute(sql_select)

    data=[]
    for record in rs:
        row=[]
        for source in range(0, len(record)):
            row.append(record[source])
        data.append(row)

    con.commit()
    cur.close()
    con.close()
    return data

def select_from_oracle2():
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()

    sql_select = '''
            select * from festival
             '''
    rs = cur.execute(sql_select)
    data=[]
    for record in rs:
        row=[]
        for source in range(0, len(record)):
            row.append(record[source])
        data.append(row)

    con.commit()
    cur.close()
    con.close()
    return data

def search_name_la_ha(name, x):
    list_lo = fa_df[fa_df[co].apply(lambda x: search(l_name,x))]
    x=list_lo['X']
    y=list_lo['Y']
    return x, y
# -----------------------------------------------------------------------------------
def mapToGrid(lats, lons, code = 0 ):
    xs = []
    ys = []
    for lat,lon in zip(lats ,lons):
        ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
        ra = re * sf / pow(ra, sn)
        theta = lon * DEGRAD - olon
        if theta > PI :
            theta -= 2.0 * PI
        if theta < -PI :
            theta += 2.0 * PI
        theta *= sn
        x = (ra * math.sin(theta)) + xo
        y = (ro - ra * math.cos(theta)) + yo
        x = int(x + 1.5)
        y = int(y + 1.5)
        xs.append(x)
        ys.append(y)
    return xs, ys
#---------------------------------------------------------------------------------------------------------------------------------
def search_ra(xs, ys):
    for x,y in zip(xs,ys) :
        lst=ra_df[(ra_df['nx']==x) & (ra_df['ny']==y)]
    return lst
# -------------------------------------------------------------------------------------------------------------------------------
# def festival(fe_df,df) :
def festival(fe_df) :

    fe_df['open_date'] = fe_df['open_date'].astype(str)
    fe_df['close_date'] = fe_df['close_date'].astype(str)
    fe_df['open_date'] = fe_df['open_date'].str.replace('-', '')
    fe_df['close_date'] = fe_df['close_date'].str.replace('-', '')
    fe_df['open_date'] = pd.to_numeric(fe_df['open_date'])
    fe_df['close_date'] = pd.to_numeric(fe_df['close_date'])
    fe_df = fe_df.sort_values(by='open_date')

    # df['fcstValue'] = df.groupby('fcstDate')['fcstValue'].apply(list)
    # df = df.drop_duplicates(subset=['fcstDate'], keep='first')
    # abc = df['fcstDate'].tolist() # 시간 데이터 가져오는 로직
    # fe_df = fe_df.drop_duplicates(subset=['f_name'], keep='last')
    fe_df = fe_df[fe_df['close_date'] > 20230000]  # 축제 종료 2023년보다 작은 경우 제외
    # fe_df = fe_df[fe_df['close_date'] > 20230719]  # 축제 종료 2023년보다 작은 경우 제외

    # print(len(fe_df))
    # fe_df = fe_df[fe_df['close_date'] > int(abc[0])] # 축제 종료 날짜가 현재보다 작은 경우 제외
    # fe_ra = fe_df[(fe_df['close_date'] > int(abc[0])) & (fe_df['open_date'] < int(abc[len(abc) - 1])) & (fe_df['close_date'] > int(abc[len(abc) - 1]))]
    # 축제 종료 날짜가 7월 20일 보다 큰거  오픈 날짜가 7월 23일보다 작은거  축제 종료 날짜가 7월 23일보다 큰거
    fe_ra = fe_df[(fe_df['close_date'] >= 20230720) & (fe_df['open_date'] <= 20230723) & (fe_df['close_date'] >= 20230723)]
    print(len(fe_ra),"개 좌표")
    # X = fe_df['X'].tolist()
    X = fe_ra['X'].tolist()
    # Y = fe_df['Y'].tolist()
    Y = fe_ra['Y'].tolist()
    print(X)
    print(Y)

    return X,Y

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
    cur = con.cursor()


    for i in range(len(df)):
        sql_insert = '''
            insert into rains(baseDate, fcstDate, nx, ny, 강수량 , 강수확률, 기온) 
            values(:baseDate, :fcstDate, :nx, :ny, :PCP, :POP,:TMP)
            '''

        baseDate = df.iloc[i]['baseDate']
        fcstDate = df.iloc[i]['fcstDate']
        nx = int(df.iloc[i]['nx'])
        ny = int(df.iloc[i]['ny'])
        PCP = float(df.iloc[i]['강수량'])
        POP = float(df.iloc[i]['강수확률'])
        TMP = float(df.iloc[i]['기온'])
        cur.execute(sql_insert,
                 (baseDate, fcstDate, nx, ny, PCP, POP, TMP)
                 )

    con.commit()
    cur.close()
    con.close()

# --------------------------------- 오라클 데이터를 가져와서 선택 열 검색 키워드의 x,y를 뽑아오는 로직 ---------------------------------
data=select_from_oracle() # 날씨 데이터
column_list_ra=['baseDate','fcstDate' ,'fcstTime' ,'nx'   ,'ny','강수량','강수확률''기온']
ra_df = pd.DataFrame(data, columns=column_list_ra)

data2=select_from_oracle2() # 축제 데이터
column_list_fa=['0','f_name','place','open_date','close_date','info','host_or','PHONE_NUMBER','ADRESS','LATITUDE','HARDNESS','X','Y','0']
fe_df = pd.DataFrame(data2, columns=column_list_fa)

#====== 검색 ===========
l_name='울산' # 키워드
co = 'f_name'     # 컬럼명
#=======================
# list_lo=fa_df[fa_df[co].apply(lambda x: search(l_name,x))]  # 컬럼명의 키워드 검색시 관련 데이터 출력
# x_list,y_list=search_name_la_ha(l_name, fa_df[fa_df[co].apply(lambda x: search(l_name,x))]) # 검색 데이터 위도 경도 출력
# x_list = x_list.tolist()
# y_list = y_list.tolist()
# #---------------------------------------------------------------------------------------------------------------
# list1=[93]
# list2=[76]
# list3 = get_request_url(list1,list2)
# column_list, all_data = json_to_df_info(list3)
# df = pd.DataFrame(all_data, columns=column_list)
x_list = [67]
y_list = [137]
# x_list, y_list = festival(fe_df,df)
# x_list, y_list = festival(fe_df) # 2023 년도 이후 축제들의 중복되는 축제명 제거 모든 X,Y 좌표 반환
raw_json = get_request_url(x_list,y_list) # 반환받은 모든 좌표로 날시 데이터 받아 제이슨 변환
column_list, all_data = json_to_df_info(raw_json)
df = pd.DataFrame(all_data, columns=column_list)
categorys = category_df(df)
print(categorys)

df_dict = categorys.to_dict(orient='records') # 데이터프레임의 모든 데이터를 딕트 형태로
print(df_dict[0])
print(len(df_dict))
# preprocessed_df_to_oracle(categorys)


#--------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------
# search_date = search_ra(la_list, ha_list)
#------------------------------------------------------------------------------------------------


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
                # initial_data = [
                #     {"company": "삼성전자", "price": 73000},
                #     {"company": "LG에너지솔루션", "price": 518000},
                #     {"company": "SK하이닉스", "price": 116700}
                # ]
                # print(type(initial_data)) # 리스트 타입 안에 딕트 타입이 있음
                # 초기 데이터를 JSON 형식으로 직렬화
                # 데이터를 텍스트 형식으로 표현 send 메서드에 문자열 형태로 데이터를 제공해야 하기 때문
                json_data = json.dumps(df_dict[0])
                print(json_data)
                # print(type(json_data)) # str 타입
                # print(json_data)
                print(len(connected))
                for client in connected:
                    try:
                        await client.send(json_data) # 데이터를 서버로 전송하고 응답을 기다림
                    except websockets.exceptions.ConnectionClosed: # 웹소켓이 닫혔을 때 실행
                        print("Client 접속 해제")

                    # while True: # 2초마다 통신 서버에 데이터 전송
                        # 최대 10% 범위 내에서 랜덤하게 상승 또는 하락
                    i = 1
                    for a,data in enumerate(df_dict) :
                        if a == 0: continue
    #                         change_percent = random.uniform(-0.1, 0.1)
    #                         data["price"] += int(data["price"] * change_percent)
    #
                        json_data = json.dumps(df_dict[i])
                        i = i + 1
                        # for client in connected:
                        try:
                            await client.send(json_data)
                            await asyncio.sleep(2)  # 2초 대기
                        except websockets.exceptions.ConnectionClosed:
                            print("Client 접속 해제")
    #
    #
    finally:
        connected.remove(websocket)  # 연결이 종료된 클라이언트를 집합에서 제거
    #

print("서버 구동 시작")
start_server = websockets.serve(handle, 'localhost', 8060) # 웹소켓 서버 객체 생성 handle 는 연결될 때 실행되는 함수
asyncio.get_event_loop().run_until_complete(start_server) # 완료 될 때 까지 함수 실행
asyncio.get_event_loop().run_forever() # 이벤트 루프를 시작하고 무한정 실행하는데 사용
