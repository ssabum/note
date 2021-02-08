import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h = h1 + h2
    m = m1 + m2

    carry = m // 60
    m = m % 60
    h += carry

    if h % 12 == 0 and h > 0:
        h = 12
    else:
        h %= 12

    print("#{} {} {}".format(tc, h, m))