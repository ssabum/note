import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: A의 사이즈
    # M: B의 사이즈
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 결과담을 리스트
    result = []
    # 각 곱의 합
    tot = 0
    # A가 클때
    if N >= M:
        for i in range(N-M+1):
            for j in range(M):
                tot += A[i+j] * B[j]
            result.append(tot)
            tot = 0
    # B가 클때
    if N < M:
        for i in range(M-N+1):
            for j in range(N):
                tot += A[j] * B[i+j]
            result.append(tot)
            tot = 0
    # 결과리스트에서 제일 큰거 찾기
    ans = result[0]

    for i in result:
        if i > ans:
            ans = i

    print("#{} {}".format(tc, ans))

