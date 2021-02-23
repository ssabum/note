import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    num, data = list(input().split())

    stack = [0]
    for i in data:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    result = stack[1:]

    print("#{}".format(tc), end=" ")
    for i in result:
        print(i, end="")
    print()
