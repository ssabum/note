import sys
sys.stdin = open('input.txt')

N = int(input())
result = 1 if N % 2 else 0
print(result)

numbers = list(map(int, input().split()))
result = sum(numbers)
print(result)

n = int(input())
m = []
for _ in range(n):
    row = list(map(int, input().split()))
    m.append(row)
result = m[1][1]
print(result)
