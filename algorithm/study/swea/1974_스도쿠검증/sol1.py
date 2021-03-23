import sys
sys.stdin = open("input.txt")

T = int(input())

# 가로검정
def row_check(arr):
    result = True
    for i in range(9):
        cnt = 0
        for j in range(9):
            cnt += arr[i][j]
        if cnt != 45:
            result = False
            return result
    return result

#  작은 네모 검정
def sm_check(arr):
    result = True
    r = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    c = [0, 3, 6, 0, 3, 6, 0, 3, 6]
    for k in range(9):
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt += arr[i + r[k]][j + c[k]]
        if cnt != 45:
            result = False
            return result
    return result


for tc in range(1, T+1):
    # 9 * 9 퍼즐판
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    # 전치 퍼즐판
    t_puzzle =  [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            t_puzzle[i][j] = puzzle[j][i]
    ans = 0
    if row_check(puzzle) == True and row_check(t_puzzle) == True and sm_check(puzzle) == True:
        ans = 1

    print("#{} {}".format(tc, ans))