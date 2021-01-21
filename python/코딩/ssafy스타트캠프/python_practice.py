import pprint

# 1. 기초 자료형
# num = 3
# print(type(num))
# string = '문자열'
# print(type(string))
# boolean = True
# print(type(boolean))
# strint_num = '3'
# print(int(strint_num)+5)

# 2. f-string(string interpolation 문자열 안에 변수 삽입)
# name = '김창규'
# print('제 이름은 ' + name + '입니다.')
# print(f'제 이름은 {name}입니다.')

# 3. List
# my_list = ['python', 'html', ' markdown']
# print(my_list[2])
# my_list[2] = 'java'
# print(my_list)

# 4. Dictionary
# age_dict = {
#     '박소현': 25,
#     '김지용': 28, # <- trailing comma : 마지막에 ,를 붙이는 이유는 수정 용이
# }
# print(age_dict['김지용'])
# print(age_dict.get('김지용'))
# age_dict['김지용'] = 50
# print(age_dict['김지용'])

# my_info = {
#     'name': 'bumhee',
#     'age': 26,
#     'msg': 'hello world!',
# }
# print(my_info)
# print(my_info['age'])

# coin = {
#     "BTC": {
#         "opening_price": "44405000",
#         "closing_price": "38806000",
#         "min_price": "36640000",
#         "max_price": "44999000",
#         "prev_closing_price": "44404000",
#         "fluctate_24H": "-7463000",
#         "fluctate_rate_24H": "-16.13"
#     },
#     "ETH": {
#         "opening_price": "1458000",
#         "closing_price": "1229000",
#         "min_price": "1100000",
#         "max_price": "1490000",
#         "prev_closing_price": "1458000",
#         "fluctate_24H": "-275000",
#         "fluctate_rate_24H": "-18.28"
#     },
#     "XRP": {
#         "opening_price": "364.5",
#         "closing_price": "311.9",
#         "min_price": "284.2",
#         "max_price": "372.7",
#         "prev_closing_price": "364.2",
#         "fluctate_24H": "-90.6",
#         "fluctate_rate_24H": "-22.51"
#     }
# }

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
# for i in range(len(coin[0]):
#     num = coin[[0][i]]
#     if coin[[0][i+1]] > num:
#         num = coin[[0][i+1]]
# print(num)
# pprint.pprint(coin['BTC']['max_price']) # <- 출력할때 모양이 이쁘게 출력
# # BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
# print(int(coin['BTC']['opening_price']) + int(coin['XRP']['opening_price']))

# 5. 기초 연산자
# 산술연산자
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(50 / 5) # 나누기
# print(50 // 3) # 몫
# print(50 % 3) # 나머지
# print(3 ** 5) # 제곱
# # 비교연산자
# print(5 == 5)
# print(5 == '3')
# print(5 != 3)
# print(5 > 3)

# 6. 조건문
# n = 0
# if n % 2 == 1:
#     print(f'{n}은 홀수입니다.')
# elif n == 0:
#     print(f'{n}은 0입니다.')
# else:
#     print(f'{n}은 짝수입니다.')

# 7. 반복문
# num = [1, 2, 3,]
# for i in num:
#     print(i)
# num = range(1,10)
# for i in num:
#     print(i)
num = range(1,10)
for i in num:
    if i % 2 == 0:
        print(f'{i}은(는) 짝수입니다.')
    else:
        print(f'{i}은(는) 홀수입니다.')