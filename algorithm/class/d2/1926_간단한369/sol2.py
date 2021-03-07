import sys
sys.stdin = open("input.txt")

# 정수 자리수 만큼 잘라서 3, 6, 9 확인
def check(n):
    digit = 0
    count = 0
    while n:
        digit = n % 10
        n = n // 10
        # if digit != 0 and digit % 3 == 0:
        if digit == 3 or digit == 6 or digit == 9:
            count += 1
    return count

N = int(input())

for i in range(1, N+1):
    count = check(i)

    # 출력
    if count:
        for j in range(count):
            print("-", end="")
        print(" ", end="")
    else:
        print(i, end=" ")




