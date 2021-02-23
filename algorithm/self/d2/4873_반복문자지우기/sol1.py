import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    data = input()
    stack = [0]

    for i in data:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    result = len(stack) - 1

    print("#{} {}".format(tc, result))