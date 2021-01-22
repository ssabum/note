import requests
import datetime
from bs4 import BeautifulSoup
import pprint

city = '광주'
key = 'ZEnJ%2F%2BhPv2A5965%2BZ0OVAqXpuZGiaQQqzoWpuu5UomOsu0Y3G%2BdKybUyrPlImH8h1tBNanqIkfNeNQDByzTXHw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName={city}&pageNo=1&numOfRows=100&returnType=json&serviceKey={key}&ver=1.0'
res = requests.get(url).json()
# pprint.pprint(res)

sido_name = res['response']['body']['items'][1]['sidoName']
pm_10 = res['response']['body']['items'][1]['pm10Value']
station_name = res['response']['body']['items'][1]['stationName']

# print(f'{sido_name}의 미세먼지 농도는 {pm_10}입니다. 측정소는 {station_name}입니다.')

# 텔레그램 메시지 전송
token = ''
api_url = f'https://api.telegram.org/bot{token}'
# 메시지 보낸 사용자의 id값 찾기
chat_id_url = f'{api_url}/getUpdates'
res2 = requests.get(chat_id_url).json()
chat_id = res2['result'][0]['message']['chat']['id']
# 메시지 보내기
text = f'{sido_name}의 미세먼지 농도는 {pm_10}입니다. 측정소는 {station_name}입니다.'
send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_url)