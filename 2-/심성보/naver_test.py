import requests
import os
import sys
import urllib.request
import json
import pandas as pd

url = 'https://openapi.naver.com/v1/datalab/search'


url_b='https://openapi.naver.com/v1/search/blog'

url_b1='https://openapi.naver.com/v1/search/blog.json'

id ='PlarbZV3yEXbIyboynxp'

pw='3az9LS7plV'
string2 = '안녕'
encText = urllib.parse.quote(string2)

url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",id)
request.add_header("X-Naver-Client-Secret",pw)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


if response_body:
    raw_json = json.loads(response_body)


def df_make(raw_json):
    all_data=[]
    column_list=['postdate','bloggername','description','link','title', 'bloggerlink']

    for record in raw_json['items']:
        row_data=[]
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data





column_list, all_data = df_make(raw_json)

df = pd.DataFrame(all_data, columns=column_list)

print(df)















