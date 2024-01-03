import threading
import time
from datetime import datetime, timedelta
from os import name

import pandas as pd
import cx_Oracle
import requests
import urllib.request

import json
# access_key = 'HVgh0GJtfha0bssIG8/oBb7dkuTWWgOnt3o47r4Wa1/SrD6VRDqJ0cOzT/6T4vL3KX4JV0bKzNZl9WqYpOdLJg=='
client_id = "2H7Pjzp4jkwrdLJON49r"
client_secret = "Lr5qMKhdX6"

def get_request_url():
    encText = urllib.parse.quote("mbti")
    url = "https://openapi.naver.com/v1/search/book?query=" + encText  # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()


    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print(rescode)

    return response_body




def abc_cut(j):
    data=[]
    num=0
    column_list = ['title','link','image','author','discount','publisher','pubdate','isbn','description']

    for record in raw_json['lastBuildDate']['total']['start']['display']['items']:
        # 이하 블럭을 자동화 해보세요.
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        data.append(row_data)


    return data

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('mbti/1111@192.168.30.28:1521/xe')
    cur = con.cursor()
    sql_insert = '''
            insert into dusts(title,link,image,author,discount,publisher,pubdate,isbn,description)
            values(:title,:link,:image,:author,:discount,:publisher,:pubdate,:isbn,:description)
            '''
    for n in range(0,len(df)):
        title = str(df.iloc[n]['title'])
        link = str(df.iloc[n]['link'])
        image =str(df.iloc[n]['image'])
        author =   str(df.iloc[n]['author'])
        discount =  int(df.iloc[n]['discount'])
        publisher =  str(df.iloc[n]['publisher'])
        pubdate = datetime(df.iloc[n]['pubdate'])
        isbn =   int(df.iloc[n]['isbn'])
        description =  str(df.iloc[n]['description'])

        cur.execute(sql_insert,
                    (title,link,image,author,discount,publisher,pubdate,isbn,description)
                    )

    con.commit()
    cur.close()
    con.close()

raw_str_json = get_request_url()
# print(raw_str_json)
# print('디버그용')

if raw_str_json:
    raw_json = json.loads(raw_str_json)

data2=[]
data2=abc_cut(raw_json)

column_list = ['title','link','image','author','discount','publisher','pubdate','isbn','description']

df = pd.DataFrame(data2[0])

df3= pd.DataFrame(data2)

print(df3)

for p in range(1,len(data2)+1):
    df.append(data2[p])




print(data2)
df2=df3.transpose()
num=0
for l in column_list:
    # print(l)
    df3.rename(columns={num:l} , inplace=True)
    num+=1

print(df2['so2Grade'])

df3=df2.set_index(column_list)
df = pd.DataFrame(data2, columns=column_list)
print(df3)
preprocessed_df_to_oracle(df3)
print()




















