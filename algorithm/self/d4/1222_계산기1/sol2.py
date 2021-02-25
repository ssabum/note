import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    # 문자열 길이
    N = int(input())
    # 문자열
    S = input()

    stack = []
    cal = []
    postfix = ""

    for i in S:
        # 스택에 숫자 추가
        if not stack and i == "+":
            stack.append(i)
        # 스택에 +가 있으면 pos에 추가하고 숫자 추가
        elif stack and i == "+":
            postfix += stack.pop()
            stack.append(i)
        # 숫자면 그냥 pos에 추가
        else:
            postfix += i
    # 스택에 남아있는 마지막 + pos에 추가
    else:
        postfix += stack.pop()

    for i in postfix:
        # 숫자면
        if i != "+":
            cal.append(int(i))
        elif i == "+":
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1+num2)

    print("#{} {}".format(tc, *cal))

