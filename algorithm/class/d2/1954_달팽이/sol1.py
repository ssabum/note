import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    num = 1
    row = 0
    col = -1
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

