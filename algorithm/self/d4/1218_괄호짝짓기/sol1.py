import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    size = int(input())
    data = input()

    stack = [0]
    result = 1

    for i in range(len(data)):
        if data[i] == "(" or data[i] == "[" or data[i] == "{" or data[i] == "<":
            stack.append(data[i])
        if data[i] == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break
        if data[i] == ">":
            if stack[-1] == "<":
                stack.pop()
            else:
                result = 0
                break
        if data[i] == "]":
            if stack[-1] == "[":
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

