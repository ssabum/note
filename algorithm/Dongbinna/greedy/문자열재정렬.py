data = input()
result = []
value = 0
# 문자를 하나씩 확인
for x in data:
    # 알파벳인 경우 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳 정렬
result.sort()
# 숫자가 하나라도 있으면 뒤에 삽입
if value != 0:
    result.append(str(value))
    
print("".join(result))