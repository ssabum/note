import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    data = list(input().split())
    num = []
    ope = ["*", "+", "-", "/"]
    result = ""
    # 마지막 마침표 제외하고 순환
    for i in data[:len(data)-1]:
        # 숫자면 스택에 저장
        if not i in ope:
            num.append(i)
        # 연산자일때
        else:
            # 스택에 숫자가 2개 미만이면 에러
            if len(num) < 2:
                result = "error"
            # 연산수행 후 스택에 저장
            else:
                num2 = num.pop()
                num1 = num.pop()
                num.append(str(eval(num1+i+num2)))
    # result가 error가 아니라면 마지막 숫자를 pop
    if result == "":
        result = num.pop()
    
    print("#{} {}".format(tc, result))