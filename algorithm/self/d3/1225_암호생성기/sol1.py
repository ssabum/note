import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))
    i = 0
    while code[-1] > 0:
        i = (i % 5) + 1
        code.append(code.pop(0) - i)
    code[-1] = 0

    print("#{} {} {} {} {} {} {} {} {}".format(tc, *code))