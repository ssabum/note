import sys
sys.stdin = open("input.txt")

T = int(input())

def spin(arr, N):
    new = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[i][j] = arr[N-1-j][i]
    return new

for tc in range(1, T+1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]

    data_90 = spin(data, N)
    data_180 = spin(data_90, N)
    data_270 = spin(data_180, N)

    print("#{}".format(tc))
    for i in range(N):
        print(''.join(data_90[i]), ''.join(data_180[i]), ''.join(data_270[i]))