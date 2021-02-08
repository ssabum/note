import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())

    def calendar(m, d):
        tot = 0
        if m == 1:
            tot = d
        elif m == 2:
            tot += 31 + d
        elif (m > 2) and (m < 9):
            tot += d + 30 * (m-1) + (m//2) - 2
        else:
            if m % 2:
                tot += d + 30 * (m-1) + ((m//2)+1) - 2
            else:
                tot += d + 30 * (m - 1) + (m // 2) - 2

        return tot

    result = calendar(m2, d2) - calendar(m1, d1) + 1

    print("#{} {}".format(tc, result))

