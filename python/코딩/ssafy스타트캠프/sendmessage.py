import requests
from bs4 import BeautifulSoup
import pprint

# 가장 최근에 메시지를 보낸 사용자에게 안녕하세요 메시지 보내기

token = ''
api_url = f'https://api.telegram.org/bot{token}'

# 메시지 보낸 사용자의 id값 찾기
chat_id_url = f'{api_url}/getUpdates'
res = requests.get(chat_id_url).json()
# pprint.pprint(res)
chat_id = res['result'][0]['message']['chat']['id']
# print(chat_id)

# 메시지 보내기
text = input('메시지를 입력하세요: ')
send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
res2 = requests.get(send_url)