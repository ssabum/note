import requests

# 요청 URL 확인 및 데이터 건네주기
name = 'bumhee'
url = f'https://api.agify.io/?name={name}'

# 요청 보내기
res = requests.get(url).json()

name = res['name']
age = res['age']
print(f'{name}님의 예상 나이는 {age}살 입니다.')