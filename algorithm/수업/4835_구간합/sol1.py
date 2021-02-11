import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    mn = 10000 * M
    mx = 0

    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += numbers[i+j]

        if tmp > mx:
            mx = tmp
        if tmp < mn:
            mn = tmp

    print("#{} {}".format(tc, mx-mn))