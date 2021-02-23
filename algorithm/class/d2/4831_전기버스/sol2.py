import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

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
                if charger[j] ==1:
                    if j-i > fuel:
                        fuel = K
                        result += 1
                    break
                if j == N-1:
                    if j > fuel:
                        fuel = K
                        result += 1
        if fuel == 0:
            result = 0
            break
    
    print("#{} {}".format(tc, result))

