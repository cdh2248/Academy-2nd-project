import rains as r
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
import threading
import time
x_coodinate = "55"
y_coodinate = "125"
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# request_time = r.get_update_time_info()
# yyyymmdd = request_time.strftime("%Y%m%d")
# hhmm = request_time.strftime("%H%M")
access_key ='HVgh0GJtfha0bssIG8/oBb7dkuTWWgOnt3o47r4Wa1/SrD6VRDqJ0cOzT/6T4vL3KX4JV0bKzNZl9WqYpOdLJg=='



# r.main_program()





def preprocessed_df_to_oracle(df):
                con = cx_Oracle.connect('project_thejoeun/1541@192.168.30.240:1521/xe')
                cur = con.cursor()
                sql_insert = '''
                        insert into rains(baseDate, baseTime, categorys,  fcstDate, fcstTime,  fcstValue,  nx,   ny) 
                        values(:baseDate, :baseTime, :categorys, :fcstDate, :fcstTime, :fcstValue, :nx, :ny)
                        '''


                baseDate = df.iloc[0]['baseDate']
                baseTime = df.iloc[0]['baseTime']
                categorys = df.iloc[0]['category']
                fcstDate = df.iloc[0]['fcstDate']
                fcstTime = df.iloc[0]['fcstTime']
                fcstValue = int(df.iloc[0]['fcstValue'])
                nx = float(df.iloc[0]['nx'])
                ny = float(df.iloc[0]['ny'])
                cur.execute(sql_insert,
                            (   baseDate, baseTime, categorys,  fcstDate, fcstTime,  fcstValue,  nx,   ny)
                            )


                con.commit()
                cur.close()
                con.close()


column_list=['baseDate', 'baseTime' ,'categorys'  ,'fcstDate' ,'fcstTime' ,'fcstValue'  ,'nx'   ,'ny']



a=    ['20230718',     1100,      'TMP'  ,'20230718'     ,'1200' ,       '26'  ,58  ,125]



# z=pd.DataFrame(a,columns=column_list)

z=pd.DataFrame(a)
y=z.transpose()
# y.rename_axis()
a=0
for cn in column_list:
        y.rename(columns={a:cn},inplace=True)
        a+=1

print(y)

preprocessed_df_to_oracle(y)
