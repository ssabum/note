import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    size = int(input())
    numbers = list(map(int, input().split()))

    max_num = numbers[0]
    min_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    result = max_num - min_num
    
    print("#{} {}".format(tc, result))

