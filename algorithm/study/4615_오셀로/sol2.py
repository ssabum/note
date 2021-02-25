import sys
sys.stdin = open("input.txt")

def init():
    mid = N // 2
    bord
    pass

def game():
    pass

def m_count(num):
    cnt = 0
    for i in range(N + 1):
        for j in range(N + 1):
            if othello[i][j] == num:
                cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    othello = [[0]*(N+1) for _ in range(N+1)]

    init()

    for i in range(M):
        c, r, color = map(int, input().split())

        game(r, c, color)

    b_cnt = m_count(1)
    w_cnt = m_count(2)

    print("#{} {} {}".format(tc, b_cnt, w_cnt))

