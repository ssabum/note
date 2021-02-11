import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    numbers = []
    for _ in range(100):
        data = list(map(int, input().split()))
        numbers.append(data)

    print(numbers)
    # print("#{} ".format(tc, ))

