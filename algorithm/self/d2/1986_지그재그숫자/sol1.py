import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 숫자 대입
    N = int(input())
    # 결과값 변수
    ans = 0

    # 1부터 N까지 돌면서 홀수는 +, 짝수는 -
    for i in range(1, N+1):
        if i % 2:
            ans += i
        else:
            ans -= i
    
    print("#{} {}".format(tc, ans))

