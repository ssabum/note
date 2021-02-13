import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 9*9 퍼즐
    data = []
    for _ in range(9):
        arr = list(map(int, input().split()))
        data.append(arr)

    ans = 0
    result = 0
    # 가로줄 검증
    tot = 0
    for i in range(9):
        for j in range(9):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    # 세로줄 검증
    tot = 0
    for i in range(9):
        for j in range(9):
            tot += data[j][i]
        if tot == 45:
            tot = 0
            ans += 1

    # 작은 사각형 검증
    tot = 0
    for i in range(0, 3):
        for j in range(0, 3):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(3, 6):
        for j in range(0, 3):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(6, 9):
        for j in range(0, 3):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(0, 3):
        for j in range(3, 6):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(3, 6):
        for j in range(3, 6):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(6, 9):
        for j in range(3, 6):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(0, 3):
        for j in range(6, 9):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(3, 6):
        for j in range(6, 9):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    tot = 0
    for i in range(6, 9):
        for j in range(6, 9):
            tot += data[i][j]
        if tot == 45:
            tot = 0
            ans += 1

    if ans == 27:
        result = 1

    print("#{} {}".format(tc, result))

