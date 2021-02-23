import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # data: 원래상태 길이는 1이상 50이하
    data = input()
    # default: 0으로 이루어진 초기값
    default = ['0' for _ in range(len(data))]

    cnt = 0
    for i in range(len(data)):
        if data[i] != default[i]:
            cnt += 1
            for j in range(i, len(data)):
                default[j] = data[i]

    print("#{} {}".format(tc, cnt))

