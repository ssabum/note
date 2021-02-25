import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # 숫자
    num = 1
    # x좌표
    row = 0
    # y좌표
    col = -1
    # 진행방향 설정을 위해
    trans = 1
    while N > 0:
        for _ in range(N):
            col += trans
            arr[row][col] = num
            num += 1
        N -= 1
        for _ in range(N):
            row += trans
            arr[row][col] = num
            num += 1
        trans *= -1

    print("#{}".format(tc))
    for i in range(len(arr)):
        print(*arr[i])

