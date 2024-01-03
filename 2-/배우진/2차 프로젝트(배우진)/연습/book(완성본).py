import threading
import time
from datetime import datetime, timedelta
from os import name
import pandas as pd
import cx_Oracle
import requests
import urllib.request
import json

client_id = "2H7Pjzp4jkwrdLJON49r"
client_secret = "Lr5qMKhdX6"
display = 50
start = 1
def get_request_url():
    encText = urllib.parse.quote("mbti")
    url = f"https://openapi.naver.com/v1/search/book.json?query={encText}&display={display}&start={start}"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
    else:
        print(rescode)

    books = json.loads(response_body)
    return books


def json_to_df_info(books_json):
    all_data = []
    column_list = ["title","link","image","author","discount","publisher","pubdate","isbn","description"]

    for record in books_json['items']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data

def preprocessed_df_to_oracle(df):

    con = cx_Oracle.connect('bwj917/1111@14.55.241.104/xe')
    cur = con.cursor()

    for i in range(len(df)) :

        sql_insert = '''
                            insert into book(제목 , 링크, 이미지, 작가, 가격, 출판사, 출시일자, 도서번호, 서술)
                            values(:title, :link, :image, :author, :discount, :publisher, :pubdate, :isbn,:description)
                            '''

        title = df.iloc[i]['title']
        link = df.iloc[i]['link']
        image = df.iloc[i]['image']
        author = df.iloc[i]['author']
        discount = int(df.iloc[i]['discount'])
        publisher = df.iloc[i]['publisher']
        pubdate = df.iloc[i]['pubdate']
        isbn = df.iloc[i]['isbn']
        description = df.iloc[i]['description']

        cur.execute(sql_insert,
                    (title, link, image, author, discount, publisher, pubdate, isbn, description)
                    )
    con.commit()
    cur.close()
    con.close()



# --------------------------------------------------------------------------------------------

books_json = get_request_url()

column_list, all_data = json_to_df_info(books_json)

df = pd.DataFrame(all_data, columns=column_list)

preprocessed_df_to_oracle(df)

# --------------------------------------------------------------------------------------------












