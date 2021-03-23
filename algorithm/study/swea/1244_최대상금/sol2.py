import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # digit: 숫자판 정보, 최대 6자리
    # change: 교환 횟수, 최대 10
    digit, change = map(int, input().split())
    digit = str(digit)
    # 교환숫자 저장
    base = {}

    for i in range(len(digit)):
        base[i] = digit[i]

    ans = []
    tot = ""
    cnt = 0
    while cnt < change:
        for j in range(len(digit)):
            for k in range(len(digit)):
                if j != k:
                    base[j], base[k] = base[k], base[j]
                    for l in base.values():
                        tot += l
                    ans.append(tot)
                tot = 0

        cnt += 1

    print(ans)

    # print("#{} ".format(tc, ))

