import os
import sys
import urllib.request
# 목적: 열 이름 재정의, 열순서 재정의
import requests
import json
from datetime import datetime, timedelta

import pandas as pd
import cx_Oracle

client_id = "2H7Pjzp4jkwrdLJON49r"
client_secret = "Lr5qMKhdX6"
encText = urllib.parse.quote("mbti")
url = "https://openapi.naver.com/v1/search/book?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print(rescode)


raw_json = json.loads(response_body)

print(raw_json['lastBuildDate'])