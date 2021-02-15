import sys
sys.stdin = open("input.txt")

# 입력 데이터
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
'''
1 2 3
4 5 6
7 8 9
'''

# 0으로 초기화
v = [[0 for _ in range(M)] for _ in range(N)]
'''
0 0 0
0 0 0
0 0 0
'''

# i행, j열
# 행 우선 조회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]

# 열 우선 조회
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]

# 지그재그 순회
for i in range(len(arr[0])):
    for j in range(len(arr)):
        # i%2 => 줄 마다 순차대로 갈지, 역순으로 갈지 정해주는 역할
        # j + (M-1-2*j) => 역순으로 갈 경우, M-1부터 -j씩 이동
        arr[i][j + (M-1-2*j) * (i%2)]

# 델타를 이용한 2차 배열 탐색
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상하좌우 대각선
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, 1, -1]
testX, testY = 0, 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for mode in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            test(arr[testX][testY])
