import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 10, M = 3
    numbers = list(map(int,input().split()))

    num_sum=[]
    max_sum=0
    min_sum=sys.maxsize
    result=0

    for j in range(N-2):
        result=numbers[j]+numbers[j+1]+numbers[j+2]
        if result > max_sum:
            max_sum = result
        if result < min_sum:
            min_sum = result

    print("#{} {}".format(tc, max_sum-min_sum))

