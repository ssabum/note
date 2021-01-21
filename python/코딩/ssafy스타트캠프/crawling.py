import requests
from bs4 import BeautifulSoup
import datetime

# 네이버 코스피
url = 'https://finance.naver.com/sise/'
# res = requests.get(url) <- 요청을 보내 모든 데이터를 받아옴
res = requests.get(url).text
# str을 구조화하여 데이터를 추출하기 쉬운 형태로 바꾸기
soup = BeautifulSoup(res, 'html.parser')
# 경로를 건네주고 원하는 정보 추출하기
kospi = soup.select_one('#KOSPI_now').text
# 현재 시간데이터 출력
now = datetime.datetime.now()

# print(f'{now}, 코스피 지수는 {kospi}입니다.')
