import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 5이상 20이하
    N = int(input())
    data = [[i for i in input()] for _ in range(N)]

    res = "NO"
    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[i][j] == "o":
                cnt += 1
                if cnt == 5:
                    res = "YES"
                    break
            else:
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if data[j][i] == "o":
                cnt += 1
                if cnt == 5:
                    res = "YES"
                    break
            else:
                cnt = 0

    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if data[i+k][j+k] == "o":
                    cnt += 1
                    if cnt == 5:
                        res = "YES"
                        break
                else:
                    cnt = 0

    data2 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data2[i][j] = data[i][N-1-j]

    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if data2[i+k][j+k] == "o":
                    cnt += 1
                    if cnt == 5:
                        res = "YES"
                        break
                else:
                    cnt = 0


    print("#{} {}".format(tc, res))