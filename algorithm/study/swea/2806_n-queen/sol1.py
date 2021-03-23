import sys
sys.stdin = open("input.txt")

T = int(input())

# 퀸 있는지 체크
def check(i):
    global case
    if i == N:
        case += 1
        return
    for j in range(N):
        if not (y[j] or dia1[i+j] or dia2[i-j+N-1]):



for tc in range(1, T+1):
    # N: 1이상 10이하 자연수
    N = int(input())
    # 가로 방향
    x = [0 for _ in range(N)]
    # 세로 방향
    y = [0 for _ in range(N)]
    # 대각선(/) 방향
    dia1 = [0 for _ in range(2*N-1)]
    # 대각선(\) 방향
    dia2 = [0 for _ in range(2*N-1)]
    # 체스판에 N개의 퀸이 있을 때, 서로 다른 두 퀸이 공격하지 못하는 경우의 수
    case = 0

    # print("#{} {}".format(tc, case))
