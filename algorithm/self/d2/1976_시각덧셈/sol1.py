import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 시간은 12시간제
    # 시는 1이상 12이하, 분은 0이상, 59이하 정수
    h1, m1, h2, m2 = map(int, input().split())
    # 더한 값을 담을 변수
    h3, m3 = 0, 0
    # 넘어가는 수
    carry = 0

    # 분 출력
    if m1 + m2 >= 60:
        m3 = m1 + m2 - 60
        carry += 1
    else:
        m3 = m1 + m2

    # 시 출력
    if h1 + h2 + carry > 12:
        h3 = h1 + h2 + carry - 12
    else:
        h3 = h1 + h2 + carry

    print("#{} {} {}".format(tc, h3, m3))

