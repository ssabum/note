import sys
sys.stdin = open("input.txt")

num = int(input())
numbers = []

for i in range(1, num+1):
    numbers.append(i)

idx = 0
i = 1
flag = len(numbers)
while flag > 1 :
    if i % 2:
        numbers.pop(0)
    else:
        numbers.append(numbers.pop(0))
    i += 1
    flag = len(numbers)

print(*numbers)
