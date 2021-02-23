import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    stick = input()
    stack = []
    result = 0

    for i in range(len(stick)):
        if stick[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if stick[i-1] == "(" : result += len(stack)
            else : result += 1
    print("#{} {}".format(tc, result))

