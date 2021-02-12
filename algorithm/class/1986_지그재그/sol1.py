import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 1 이상 10 이하 정수
    N = int(input())

    tot = 0

    for i in range(1, N+1):
        if not i % 2:
            tot -= i
        else:
            tot += i

    print("#{} {}".format(tc, tot))

