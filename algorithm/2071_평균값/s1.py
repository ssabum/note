import sys
sys.stdin = open('input.txt')

N = int(input())

for num in range(1, N+1):
    numbers = list(map(int, input().split()))
    sum = 0
    leng = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        leng += 1
        result = round(sum / leng)

    print('#{} {}'.format(num, result))