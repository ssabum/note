import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = sorted(list(map(int, input().split())))
    # 0초부터 마지막 시간의 손님까지 time
    result = "Possible"
    now = 0
    for i in range(N):
        now += (time[i] // M) * K - (i+1)
        if now < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc, result))
