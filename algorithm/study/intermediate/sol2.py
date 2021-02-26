import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    map = [list(input()) for _ in range(N)]

    AnserN = 0
    for i in range(N):
        for j in range(N):
            # 기지국일 경우
            if map[i][j] != "X" and map[i][j] != "H":
                for k in range(1, ord(map[i][j] - ord("A") + 2)):


    print("#{} {}".format(tc, AnserN))
