import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    num = int(input())
    data = list(map(int, input().split()))

    max_num = data[0]
    for i in data:
        if i > max_num:
            max_num = i # 7

    gravity = [0] * max_num # 7

    for _ in range(max_num): # 7
        for i in range(num):
            list_g = [0] * num # 9
            if data[i] >= 1:
                data[i] -= 1
                list_g[i] += 1
            for i in list_g:
                count = 0
                if i == 0:
                    count += 1
                gravity.append(count)

    max_gravity = 0
    for i in gravity:
        if i > max_gravity:
            max_gravity = i

    print("#{} {}".format(tc, max_gravity))

