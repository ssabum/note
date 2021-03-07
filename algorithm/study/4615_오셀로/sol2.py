# 오셀로
import sys
sys.stdin = open("input.txt")

# 기본 셋팅
def init():
    mid = N // 2
    othello[mid+1][mid+1] = othello[mid][mid] = 2
    othello[mid+1][mid] = othello[mid][mid+1] = 1

# 8방향 탐색
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
def game(r, c, color):
    othello[r][c] = color
    # 8방향 검사
    for i in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            # 바운더리 체크
            if nr <= 0 or nr > N or nc <= 0 or nc > N: break
            # 빈칸을 만나면 탈출
            if othello[nr][nc] == 0: break
            # 같은 색을 만날 경우
            if othello[nr][nc] == color:
                # 그 사이에 있는 다른 색의 돌을 뒤집기
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] = color
                break

# 돌개수 세기
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

    # 기본세팅을 하기위한 함수
    init()

    for _ in range(M):
        c, r, color = map(int, input().split())
        game(r, c, color)

    b_cnt = m_count(1)
    w_cnt = m_count(2)

    print("#{} {} {}".format(tc, b_cnt, w_cnt))

