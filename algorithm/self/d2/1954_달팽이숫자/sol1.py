import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N * N 행렬
    N = int(input())
    # 행렬에 들어갈 1부터 N^2까지 숫자
    number = [i for i in range(1, N**2+1)]
    # 결과 담을 리스트
    ans = [[0 for i in range(N)] for i in range(N)]

    for i in range(N):
        ans[0][i] = number[i]
    for i in range(1, N):
        ans[i][-1] = number[N+i-1]





    # print("#{} ".format(tc, ))

