import sys
sys.stdin = open("input.txt")

# 정수 자리수 만큼 잘라서 3, 6, 9 확인
def check(n):
    digit = 0
    cnt = 0
    while n:
        digit = n % 10
        n = n // 10
        if digit != 0 and digit % 3 == 0:
            cnt += 1
    return cnt

N = int(input())

for i in range(1, N+1):
    cnt = check(i)

    # 출력
    if cnt:
        for j in range(cnt):
            print("-", end="")
        print(" ", end="")
    else:
        print(i, end=" ")




