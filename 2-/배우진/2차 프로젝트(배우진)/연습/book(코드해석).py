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
display = 50 # 검색시 가지고 올 데이터의 갯수
start = 1 # 검색 시작 위치 설정 첫번째가 1  <- 이 부분 수정시 기능 작동은 하나 데이터 베이스에 저장순서가 뒤죽박죽이 됨
def get_request_url():
    # urllib.parse 모듈은 url 구문분석, 요소 인코딩 및 디코딩 등 url 관련 작업을 위한 모듈
    encText = urllib.parse.quote("mbti") # quote 주어진 문자열의 특수 문자를 해당하는 url 인코딩 문자로 바꿔준다
    # 일반 문자열만 출력시 -> 'mbti' = 'mbti'    특수문자 포함하여 출력시 'mbti#@$' = 'mbti%23%40%24'  <- HTTP가 읽을 수 있는 문자로 인코딩

    url = f"https://openapi.naver.com/v1/search/book.json?query={encText}&display={display}&start={start}"# 도서url 에 url인코딩이 된 검색어 문자열을 붙임
    # url = f"https://openapi.naver.com/v1/search/book_adv.json?d_titl={encText}&display=10&start=1" # 상세 검색

    # urllib.request 는 HTTP 요청을 만들고  URL처리, 웹리소스와 상호 작용하기 위한 파이썬 표준 모듈
    request = urllib.request.Request(url) # url내용을 토대로 HTTP 요청 객체를 생성하는 함수
    # <urllib.request.Request object at 0x0000017791BF7A00>  <- 생성된 HTTP 요청 객체

    # HTTP의 Request(요청) 구조는 Start Line, Headers, Body 로 구성
    # Headers는 해당 Request(요청)에 대한 추가 정보를 담고 있는 부분
    # 키와 밸류의 형태로 구성 되어 있음
    # 밑 코드는 HTTP headers 부분에 정보를 추가하는 메서드 헤더 이름과 헤더 값 두가지 인수를 사용
    request.add_header("X-Naver-Client-Id", client_id) # Naver API 클라이언트 ID에 대한 특정 헤더 값으로 client_id 를 넣겠다는 것
    request.add_header("X-Naver-Client-Secret", client_secret) # 생성 해 놓았던 HTTP 요청 객체의 Headers 부분에 id, secret 이 담기고 있는 것

    response = urllib.request.urlopen(request) # 서버에 요청 HTTP를 보내고 응답 객체를 반환하는 함수
    # <http.client.HTTPResponse object at 0x000002376F6EB0A0> <- 응답 받은 반환 객체 요 객체 안에 우리가 필요한 데이터들이 있음 사용하기 위해 가공이 필요함

    rescode = response.getcode() # 응답 객체의 HTTP 상태 코드를 반환
                                 # 앞으로 많이 접할 수 있어 몇가지 코드는 기억해두면 좋음
                                 # 200(정상), 404(찾을수없음), 500(내부 서버 오류) 등 여러 코드들이 더 있음

    if (rescode == 200): # 응답 객체의 상태 코드가 200(정상)일 때 True
        response_body = response.read() # read(): 응답 객체의 데이터를 바이트로 읽어서 반환하는 응답 객체의 함수
    #   response_body.decode('utf-8')   # 지정된 인코딩을 사용해서 바이트열을 문자열로 디코딩 하는 메서드
                                        # 제이슨 형태로 변환하는 것이면 이 과정은 거치지 않아도 됨
    else:
        print(rescode) # 응답 객체의 상태코드가 200(정상)이 아닐 때 상태코드 반환

    books = json.loads(response_body) # 반환 객체 안에 있는 JSON 형식 문자열을 해당 Python 개체로 반환(딕셔너리) json은 데이터 교환 형식을 말하는 것

    return books


def json_to_df_info(books_json):
    all_data = [] # 모든 행 데이터를 담을 배열 생성
    column_list = ["title","link","image","author","discount","publisher","pubdate","isbn","description"] # 제이슨에 있는 키 값과 동일해야함

    for record in books_json['items']: # 제이슨의 items의 요소들을 가지고 실행 현재 10개의 요소가 있고 1개의 요소가 1개의 행을 이룬다고 보면 됨
        row_data = [] # 각 행 데이터를 담을 배열
        for column_data in column_list:
            row_data.append(record.get(column_data)) # 제이슨의 요소에서 column_list의 이름을 키 값으로 하여 밸류값을 가져온 후 row_data 배열에 삽입
        all_data.append(row_data) # 각 행의 리스트를 모든 행 리스트에 삽입 (2차원 배열 생성)

    return column_list, all_data # 컬럼리스트와 행 데이터 리턴

def preprocessed_df_to_oracle(df):
        # cx_Oracle.connect('사용자이름/패스워드@아이피 또는 localhost/서비스 이름')
        # 문자열을 인수로 사용하여 oracle 와 상호작용 할 수 있는 연결객체를 반환
        # 연결이 설정되면 SQL문 실행, 데이터 쿼리 또는 테이블에 레코드 삽입 등 가능
        # 작업을 완료한 후에는 모든 리소스 해제를 위해 연결을 닫는 것이 중요
    con = cx_Oracle.connect('bwj917/1111@14.55.241.104/xe') # Oracle 데이터 베이스와 연결
    cur = con.cursor() # SQL문을 실행, 데이터베이스 작업을 수행 하는데 사용 할 수 있는 커서 객체를 생성

    for i in range(len(df)) :

        # SQL 문법을 해당 변수에 저장
        # 테이블 명('book')과 데이터를 삽입할 컬럼명을 지정
        # 해당 컬럼에 삽입할 값을 지정하는 부분
        sql_insert = '''
                            insert into book(제목 , 링크, 이미지, 작가, 가격, 출판사, 출시일자, 도서번호, 서술)
                            values(:title, :link, :image, :author, :discount, :publisher, :pubdate, :isbn,:description)
                            '''
        # 밸류 값을 지정하기 위해 데이터프레임에서 선택 열의 i(행) 값을 전처리
        title = df.iloc[i]['title']
        link = df.iloc[i]['link']
        image = df.iloc[i]['image']
        author = df.iloc[i]['author']
        discount = int(df.iloc[i]['discount']) # 숫자는 int로 형변환
        publisher = df.iloc[i]['publisher']
        # pubdate = int(df.iloc[i]['pubdate']) 널 값이 있는 데이터가 있어 형변환 불가 전처리 후 사용 가능
        pubdate = df.iloc[i]['pubdate']
        # isbn = int(df.iloc[i]['isbn'])  위와 같음
        isbn = df.iloc[i]['isbn']
        description = df.iloc[i]['description']

        # SQL 문을 실행하기 위한 메서드
        # sql_insert는 book 테이블에 데이터를 삽입하는 SQL문
        # 밑 코드는 테이블에 삽입할 실제 값을 포함하는 튜플 print(title) ->  MBTI 공부법 (최상위 1%의 비밀)
        # (title, link, image, author, discount, publisher, pubdate, isbn, description)
        cur.execute(sql_insert,
                    (title, link, image, author, discount, publisher, pubdate, isbn, description)
                )

    con.commit()  # 변경된 내용을 커밋하기 위한 메서드
    cur.close() # SQL문을 실행하기 위한 커서객체의 리소스 , 메모리 해제
    con.close() # 모든 리소스를 해제 하고 데이터베이스에 대한 연결 종료



# --------------------------------------------------------------------------------------------

books_json = get_request_url() # 요청한 검색어를 제이슨으로 받는 함수

column_list, all_data = json_to_df_info(books_json) # 제이슨을 컬럼과 행 데이터로 나누는 함수

df = pd.DataFrame(all_data, columns=column_list) # 데이터 프레임 생성

preprocessed_df_to_oracle(df) # 생성한 데이터프레임을 오라클로 전송하는 함수

# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------





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










