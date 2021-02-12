import sys
sys.stdin = open("input.txt")
# N: 숫자들의 개수 / 항상 홀수
N = int(input())

numbers = list(map(int, input().split()))

for i in range(len(numbers)-1, 0, -1):
    for j in range(0, i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

result = numbers[(len(numbers) // 2)]

print(result)

