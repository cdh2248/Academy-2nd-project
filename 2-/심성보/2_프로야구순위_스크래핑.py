from bs4 import BeautifulSoup
import urllib.request
import os
import pandas as pd

# Callable 관련 에러가 나면 추가해야 되는 코드
import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable


# 네이버에서 '프로야구 순위' 검색한 URL
html = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%94%84%EB%A1%9C%EC%95%BC%EA%B5%AC+%EC%88%9C%EC%9C%84')
soup = BeautifulSoup(html, 'html.parser')

# html 태그가 언제 바뀔지 모르니 스크래핑에 사용했던 기술을 기억하기 위해서 html을 저장하는 습관을 들이자.
file_path = '프로야구순위.html'
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
        print("HTML 파일이 저장되었습니다.")

# 테이블을 찾습니다.
# table = soup.find('div', id="teamRankTabPanel_0").table.tbody
table = soup.find('div', id="teamRankTabPanel_0").table
# print(table)
# 테이블의 각 행을 추출하여 리스트에 저장합니다.

thead = table.thead

head_list=[]
for col in thead.find_all('th'):
    head_list.append(col.text)
print(head_list)


tbody = table.tbody
data = []
rank = 1
for tr in tbody.find_all('tr'):
    row = []
    is_first = True
    for col in tr.find_all('td'):
        # 팀명이 a.text가 아니라 동일하게 td.text 인점을 기억하자 (Debug를 통해 파악)
        if is_first:
            row.append(rank)
            rank += 1
            is_first = False
            row.append(col.text.strip())
            continue
        row.append(col.text.strip())
    data.append(row)

print(data)

df = pd.DataFrame(data=data, columns=head_list)
pass
