import threading
import time
from datetime import datetime, timedelta
from os import name

import pandas as pd
import cx_Oracle
import requests
import urllib.request
import json

client_id = "2H7Pjzp4jkwrdLJON49r"   # 클라이언트 아이디
client_secret = "Lr5qMKhdX6"         # 클라이언트 시크릿

def get_request_url(): # 요청한 검색어를 제이슨으로 받는 함수
    encText = urllib.parse.quote("mbti")
    print(urllib.parse.quote("mbti"))
    url = "https://openapi.naver.com/v1/search/book?query=" + encText  # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    #     response_body.decode('utf-8')
    # else:
    #     print(rescode)

    books = json.loads(response_body)

    return books

def json_to_df_info(books_json): # 딕트
    all_data = []
    column_list = ["title","link","image","author","discount","publisher","pubdate","isbn","description"]

    for record in books_json['items']: # 행 데이터 생성
        # 이하 블럭을 자동화 해보세요.
        row_data = []
        for column_data in column_list: # 컬럼 생성
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data

def preprocessed_df_to_oracle(df):
    print('hi')
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()

    sql_insert = '''
            insert into book(제목 , 링크, 이미지, 작가, 가격, 출판사, 출시일자, 도서번호, 서술)
            values(:title, :link, :image, :author, :discount, :publisher, :pubdate, :isbn,:description)
            '''
    title = df.iloc[0]['title']
    link = df.iloc[0]['link']  # int 값에 대해서는 int 형으로 변환해줘야 한다.
    image = df.iloc[0]['image']
    author = df.iloc[0]['author'] # 현재 데이터 프레임의 행인덱스가 date_time이므로 loc가 안된다.
    discount = int(df.iloc[0]['discount'])
    publisher = df.iloc[0]['publisher']
    pubdate = int(df.iloc[0]['pubdate'])
    isbn = int(df.iloc[0]['isbn'])
    description = df.iloc[0]['description']

    cur.execute(sql_insert,
                (title, link, image, author, discount, publisher, pubdate, isbn,description)
                )

    con.commit()
    cur.close()
    con.close()

books_json = get_request_url()
column_list, all_data = json_to_df_info(books_json)
df = pd.DataFrame(all_data, columns=column_list)
preprocessed_df_to_oracle(df)





# def abc_cut(j):
#     data=[]
#     num=0
#     column_list = ['title','link','image','author','discount','publisher','pubdate','isbn','description']
#
#     for record in raw_json['lastBuildDate']['total']['start']['display']['items']:
#         # 이하 블럭을 자동화 해보세요.
#         row_data = []
#         for column_data in column_list:
#             row_data.append(record.get(column_data))
#         data.append(row_data)
#
#
#     return data
#
# def preprocessed_df_to_oracle(df):
#     con = cx_Oracle.connect('mbti/1111@192.168.30.28:1521/xe')
#     cur = con.cursor()
#     sql_insert = '''
#             insert into dusts(title,link,image,author,discount,publisher,pubdate,isbn,description)
#             values(:title,:link,:image,:author,:discount,:publisher,:pubdate,:isbn,:description)
#             '''
#     for n in range(0,len(df)):
#         title = str(df.iloc[n]['title'])
#         link = str(df.iloc[n]['link'])
#         image =str(df.iloc[n]['image'])
#         author =   str(df.iloc[n]['author'])
#         discount =  int(df.iloc[n]['discount'])
#         publisher =  str(df.iloc[n]['publisher'])
#         pubdate = datetime(df.iloc[n]['pubdate'])
#         isbn =   int(df.iloc[n]['isbn'])
#         description =  str(df.iloc[n]['description'])
#
#         cur.execute(sql_insert,
#                     (title,link,image,author,discount,publisher,pubdate,isbn,description)
#                     )
#
#     con.commit()
#     cur.close()
#     con.close()
#
# raw_str_json = get_request_url()
# # print(raw_str_json)
# # print('디버그용')
#
# if raw_str_json:
#     raw_json = json.loads(raw_str_json)
#
# data2=[]
# data2=abc_cut(raw_json)
#
# column_list = ['title','link','image','author','discount','publisher','pubdate','isbn','description'
# ]
#
# df = pd.DataFrame(data2[0])
# df3= pd.DataFrame(data2)
# print(df3)
# # for p in range(1,len(data2)+1):
# #     df.append(data2[p])
#
#
#
#
# # print(data2)
# # df2=df3.transpose()
# num=0
# for l in column_list:
#     # print(l)
#     df3.rename(columns={num:l} , inplace=True)
#     num+=1
#
# # print(df2['so2Grade'])
#
# # df3=df2.set_index(column_list)
# # df = pd.DataFrame(data2, columns=column_list)
# print(df3)
# preprocessed_df_to_oracle(df3)
# # print()
# #
#
#
#
#
#
#
#
#
#










