'''
리스트의 총곱

사용자가 입력한 정수 num을 기준으로, 1~num으로 이루어진 리스트의 총 곱을 구하는 함수를

1. `for`문을 사용하여
2. `while`문을 사용하여

작성하시오.
'''

# for문만 사용하여 풀기
def mul_with_for(numbers):
    res = 1
    for i in numbers:
        res *= i
    return res

# while문만 사용하여 풀기
def mul_with_while(numbers):
    res = 1
    i = 1
    while i <= num:
        res *= i
        i += 1
    return res


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    num = int(input('정수를 입력하세요'))
    numbers = list(range(1, num+1))

    # 아래 두코드 모두 in 4 => out 24 / in 5 => out 120 를 만족해야 합니다.
    print(mul_with_for(numbers))
    print(mul_with_while(numbers))