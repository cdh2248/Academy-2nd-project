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


data=select_from_oracle() # 날씨 데이터
column_list_ra=['baseDate', 'baseTime' ,'categorys'  ,'fcstDate' ,'fcstTime' ,'fcstValue'  ,'nx'   ,'ny']
ra_df = pd.DataFrame(data, columns=column_list_ra)

data2=select_from_oracle2() # 축제 데이터
column_list_fa=['f_name','place','open_date','close_date','info','host_or','PHONE_NUMBER','ADRESS','LATITUDE','HARDNESS','X','Y','0']
fa_df = pd.DataFrame(data2, columns=column_list_fa)

fa_df['open_date'] = fa_df['open_date'].astype(str)
fa_df['close_date'] = fa_df['close_date'].astype(str)
fa_df['open_date'] = fa_df['open_date'].str.replace('-', '')
fa_df['close_date'] = fa_df['close_date'].str.replace('-', '')
fa_df['open_date'] = pd.to_numeric(fa_df['open_date'])
fa_df['close_date'] = pd.to_numeric(fa_df['close_date'])
fe_df = fa_df.sort_values(by='open_date')
fe_df = fe_df[fe_df['close_date'] > 20230719]
fe_ra = fe_df[(fe_df['close_date'] > 20230719) & (fe_df['open_date'] < 20230723) & (fe_df['close_date'] > 20230323)]
X = fe_ra['X'].tolist()
Y = fe_ra['Y'].tolist()
