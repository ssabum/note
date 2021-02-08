import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):

    numbers = input()

    cnt = [0] * 12
    for number in numbers:
        cnt[int(number)] += 1

    i = 0
    tri = 0
    step = 0

    while i < 10:
        if cnt[i] >= 3:
            tri += 1
            cnt[i] -= 3
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

