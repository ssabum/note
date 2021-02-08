import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    numbers = list(map(int, input()))

    cnt = [0] * 10
    for number in numbers:
        cnt[number] += 1

    tri, step, i, result = 0, 0, 0, 0
    while i < 8:
        if cnt[i] >= 3:
            tri += 1
            cnt[i] -= 1
            continue
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            step += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue
        i += 1

    result = tri + step

    if result == 2:
        print('#{} 1'.format(tc))
    else:
        print("#{} 0".format(tc))

