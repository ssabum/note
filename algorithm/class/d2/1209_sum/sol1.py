import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T = int(input())
    ans = 0
    arr = []
    for _ in range(100):
        num = list(map(int, input().split()))
        arr.append(num)

    sum_list = []

    # 가로줄 랍
    for i in range(len(arr)):
        tot = 0
        for j in range(len(arr[i])):
            tot += arr[i][j]
        sum_list.append(tot)

    # 세로줄 합
    for j in range(len(arr[0])):
        tot = 0
        for i in range(len(arr)):
            tot += arr[i][j]
        sum_list.append(tot)

    # 대각선 정방향 합
    n, x, y, tot = 0, 0, 0, 0
    while n < len(arr[0]):
        tot += arr[x][y]
        x += 1
        y += 1
        n += 1
    sum_list.append(tot)

    # 대각선 역방향 합
    n, x, y, tot = 0, len(arr[0])-1, len(arr[0])-1, 0
    while n < len(arr[0]):
        tot += arr[x][y]
        x -= 1
        y -= 1
        n += 1
    sum_list.append(tot)

    for i in range(len(sum_list)-1, 0, -1):
        for j in range(0, i):
            if sum_list[j] > sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

    ans = sum_list[-1]
    print("#{} {}".format(tc, ans))

