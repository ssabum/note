import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N번 정류장 까지 이동
    # k: 한번 이동시 최대 이동할 수 있는 정류장 수
    # M: 충전지가 설치된 M개의 정류장 개수
    # station: 충전지가 설치된 정류장 리스트
    # charger: 충전기 위치 리시트
    # result: 충전 횟수
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    charger = [0] * N

    for i in range(N):
        if i in station:
            charger[i] = 1
            continue
        charger[i] = 0

    result = 0
    fuel = K
    i = 0

    while i < N-1:
        fuel -= 1
        i += 1

        if charger[i] == 1:
            for j in range(i+1, N):
                if charger[j] == 1:
                    if j-i > fuel:
                        fuel = K
                        result += 1
                    break
                if j == N-1:
                    fuel = K
                    result += 1
        if fuel == 0:
            result = 0
            break

    print("#{} {}".format(tc, result))

