import requests
import json
from datetime import datetime, timedelta

def get_request_url(x_coodinate, y_coodinate):
    access_key = 'bwc3DJ6DBSdRpgK4ZBeKvvb42M0KALQDAzhEhe8AkUP9nwc9VHoO5r6OxJfBrnuNK76bfwk2hAmqEJWaYL+4ag=='
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    raw_json = []
    i = 1
    request_time = get_update_time_info()
    yyyymmdd = request_time.strftime("%Y%m%d")
    hhmm = request_time.strftime("%H%M")

    for x,y in zip(x_coodinate,y_coodinate):
        params = {'serviceKey': access_key ,
                  'numOfRows' : 1000,
                  'pageNo' : 1,
                  'dataType': 'JSON',
                  'base_date':yyyymmdd,
                  'base_time':hhmm,
                  'nx':x,
                  'ny':y
        }
        response = requests.get(url, params=params)
        if response :
            raw_json.append(json.loads(response.text))  # 제이슨형식의 문자열을 파이썬의 딕트 타입으로 변환
            print(response)
            print(i)
            i = i + 1
    return raw_json


def get_update_time_info():
    now = datetime.now()  # 2023-07-10 13:25:30.597281 //현재 local date와 time을 리턴
    num = [2, 5, 8, 11, 14, 17, 20, 23]
    num2 = [0,3,6,9,12,15,18,21]
    num3 = [1,4,7,10,13,16,19,22]
    for number in range(len(num)) :

        if now.hour == num[number]:
            print(f"현재 시간대 정보로 업데이트 합니다.: {now}")
            return now # 현재 시간대 리턴
        elif now.hour == num2[number]:
            update_cycle_min = timedelta(hours=1)
            lastest_time = now - update_cycle_min
            print(f"이전 시간대 정보로 업데이트 합니다.: {lastest_time}")
            return lastest_time # 이전 시간대 리턴
        elif now.hour == num3[number]:
            update_cycle_min = timedelta(hours=2)
            lastest_time = now - update_cycle_min
            print(f"이전 시간대 정보로 업데이트 합니다.: {lastest_time}")
            return lastest_time  # 이전 시간대 리턴





