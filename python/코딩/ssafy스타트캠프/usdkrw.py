# 크롤링 할 때 필요한 라이브러리
import requests
import datetime
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
# 요청보내기
res = requests.get(url).text
# 응답받은 값을 추출하기 쉬운 형태로 구조화
soup = BeautifulSoup(res, 'html.parser')

usdkrw = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
now = datetime.datetime.now()

print(f'{now}, 원달러 환율은 {usdkrw}원 입니다.')

