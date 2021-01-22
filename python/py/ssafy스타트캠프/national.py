import requests
import pprint

name = 'michael'
url = f'https://api.nationalize.io/?name={name}'

res = requests.get(url).json()
pprint.pprint(res)
name = res['name']
country = res['country'][0]['country_id']
pro = round(res['country'][0]['probability'] * 100, 2)
print(f'{name}님의 예상 국적은 {pro}확률로 {country}입니다.')
