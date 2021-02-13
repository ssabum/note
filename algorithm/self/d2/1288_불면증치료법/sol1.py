import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 1이상 1000000이하
    N = int(input())
    count = 0
    num = 1
    data = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

    while True:
        for i in str(N):
            data[int(i)] += 1
            count += 1
            num += 1
            if not False in data.values():
                break
            N = num * N
    
    print("#{} {}".format(tc, count))

