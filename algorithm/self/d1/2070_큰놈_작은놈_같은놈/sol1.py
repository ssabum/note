import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 각 수는 0이상 10000이하의 정수
    a, b = map(int, input().split())
    if a > b:
        result = ">"
    elif a == b:
        result = "="
    else:
        result = "<"

    print("#{} {}".format(tc, result))

