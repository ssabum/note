import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    size = int(input())
    data = list(map(int, input().split()))

    gravity = [0] * size
    for i in range(len(data)):
        count = 0
        for j in range(len(data)):
            if data[i] > data[j]:
                count += 1
        gravity[i] = count

    max_gravity = 0
    for i in gravity:
        if i > max_gravity:
            max_gravity = i

    print("#{} {}".format(tc, max_gravity))

