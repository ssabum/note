import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    data = input()
    stack = [0]
    result = 1

    for i in range(len(data)):
        if data[i] == "(" or data[i] == "{":
            stack.append(data[i])

        if data[i] == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break

        if data[i] == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                result = 0
                break

    if len(stack) > 1:
        result = 0

    print("#{} {}".format(tc, result))