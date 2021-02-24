import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    num, data = list(input().split())

    stack = []
    for i in data:
        if not stack or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()

    print("#{} {}".format(tc, ''.join(stack)))