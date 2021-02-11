import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 더한 결과값을 담은 리스트
    result = []
    plus = 0

    # A가 큰 경우
    if N >= M:
        for i in range(N-M+1):
            for j in range(M):
                plus += A[i+j] * B[j]
            result.append(plus)
            plus = 0
    # B가 큰 경우
    if M > N:
        for i in range(M-N+1):
            for j in range(N):
                plus += B[i+j] * A[j]
            result.append(plus)
            plus = 0

    max_result = result[0]
    for i in result:
        if i > max_result:
            max_result = i

    print("#{} {}".format(tc, max_result))

