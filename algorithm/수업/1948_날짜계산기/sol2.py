import sys
sys.stdin = open("input.txt")

T = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    # 일 계산
    d = d2 - d1 + 1

    # 월 계산
    ans = 0
    for i in range(m1, m2):
        ans += day[i]

    ans += d
    
    print("#{} {}".format(tc, ans))

