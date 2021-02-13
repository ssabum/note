import sys
sys.stdin = open("input.txt")

# 자릿수별로 3, 6, 9가 몇 번 들어있는지 확인
def check(n):
    # digit: 각 자리 숫자
    digit = 0
    # n에 3, 6, 9가 몇 번 있는지
    count = 0
    while n:
        digit = n % 10
        n = n // 10
        if digit != 0 and digit % 3 == 0:
            count +=1
    return count

# 숫자 입력
N = int(input())

for i in range(1, N+1):
    count = check(i)

    # 만약 카운트가 되면 갯수에 맞춰서 "-"출력
    if count:
        for i in range(count):
            print("-", end="")
        print(" ", end="")
    # 카운트 안되면(3, 6, 9 숫자가 없으면) 그냥 숫자 출력
    else:
        print(i, end=" ")

