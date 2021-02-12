import sys
sys.stdin = open("input.txt")

data = input()

result = []

for i in data:
    if i.islower():
        result.append(ord(i) - 96)
    result.append(ord(i) - 64)

for i in result:
    print(i, end=" ")



