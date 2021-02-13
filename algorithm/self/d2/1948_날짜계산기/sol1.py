import sys
sys.stdin = open("input.txt")

T = int(input())

data = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(1, T+1):
    # 날짜 저장
    m1, d1, m2, d2 = map(int, input().split())
    # 결과값 변수
    ans = 0
    # date 계산
    ans += d2 - d1 + 1
    # month 계산
    for i in range(m1, m2):
        ans += data[i]

    print("#{} {}".format(tc, ans))

