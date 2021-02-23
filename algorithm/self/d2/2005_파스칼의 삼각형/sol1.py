import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 1이상 10이하 정수
    N = int(input())
    base = [[1] * i for i in range(1, N+1)]

    for r in range(N):
        for c in range(r+1):
            if r > 1 and 0 < c < r:
                base[r][c] = base[r-1][c-1] + base[r-1][c]

    print("#{}".format(tc))
    for i in base:
        print(*i)

