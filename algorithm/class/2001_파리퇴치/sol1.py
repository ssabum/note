import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    # 큰 사각형 순회, (x, y) => 시작 좌표
    for x in range(N-M+1):
        for y in range(N-M+1):
            # 작은 사각형
            sum_value = 0
            for i in range(M):
                for j in range(M):
                    sum_value += arr[x+i][y+j]
            if sum_value > max_value:
                max_value = sum_value

    print("#{} {}".format(tc, max_value))