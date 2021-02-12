import sys
sys.stdin = open("input.txt")

T = int(input())

result = []

for i in range(T+1):
    result.append(2 ** i)

for i in result:
    print(i, end=" ")


