import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    data = list(map(int, input().split()))
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    result = data[-1]
    
    print("#{} {}".format(tc, result))

