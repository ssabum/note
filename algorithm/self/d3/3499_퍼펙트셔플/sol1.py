import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 1이상 1000이하 자연수
    N = int(input())
    data = input().split()

    result = []
    data1 = data[:int(len(data)/2+0.5)]
    data2 = data[int(len(data)/2+0.5):]

    for i in range(len(data2)):
        result.append(data1[i])
        result.append(data2[i])

    if len(data1) != len(data2):
        result.append(data1[-1])

    print("#{}".format(tc), end=" ")
    for i in result:
        print(i, end=" ")
    print()

