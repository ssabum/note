import sys
sys.stdin = open("input.txt")

T = int(input())

# 오른쪽
dr = [0,1,1,1]
dc = [1,1,0,-1]

def check():
    for i in range(N):
        for j in range(N):
            # 4방향 순환
            for k in range(4):
                o_cnt = 0
                nr, nc = i, j
                while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == "o":
                    o_cnt += 1
                    if o_cnt == 5:
                        return "YES"
                    nr += dr[k]
                    nc += dc[k]
    return "NO"

for tc in range(1, T+1):
    N = int(input())
    # 오목판 입력
    arr = [input() for _ in range(N)]
    
    print("#{} {}".format(tc, check()))

