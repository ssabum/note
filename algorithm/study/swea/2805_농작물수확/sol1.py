import sys
sys.stdin = open("input.txt")

T = int(input())

def check(arr, n):
    # 맨 위 중간부터 시작
    mid = n // 2
    s = e = mid
    cnt = 0
    for i in range(N):
        for j in range(s, e+1):
            cnt += arr[i][j]
        # 가운데 꽉 차면 이후로 1칸씩 감소
        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    return cnt

for tc in range(1, T+1):
    # N * N 농장, 항상 홀수
    N = int(input())
    # 수확할 수 있는 농작물
    data = [[int(i) for i in input()] for _ in range(N)]

    result = check(data, N)

    print("#{} {}".format(tc, result))

