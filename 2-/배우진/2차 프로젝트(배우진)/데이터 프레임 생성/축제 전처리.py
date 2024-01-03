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




NX = 149            ## X축 격자점 수
NY = 253            ## Y축 격자점 수
Re = 6371.00877     ##  지도반경
grid = 5.0          ##  격자간격 (km)
slat1 = 30.0        ##  표준위도 1
slat2 = 60.0        ##  표준위도 2
olon = 126.0        ##  기준점 경도
olat = 38.0         ##  기준점 위도
xo = 210 / grid     ##  기준점 X좌표
yo = 675 / grid     ##  기준점 Y좌표

first = 0



if first == 0 :
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI


    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

fe = pd.read_csv("../축제.csv", encoding='euc-kr')
la_list = fe['위도'].tolist()
ha_list = fe['경도'].tolist()

x_list,y_list = mapToGrid(la_list,ha_list)

fe['X'] = x_list
fe['Y'] = y_list
fe.to_csv('축제(좌표).csv', index=False, encoding= 'utf-8-sig')
print(fe)

