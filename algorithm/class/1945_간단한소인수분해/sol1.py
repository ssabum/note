import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 입력 숫자 데이터
    # N은 2이상 10000000 이하
    N = int(input())

    # 2, 3, 5, 7, 11의 지수
    a, b, c, d, e = 0, 0, 0, 0, 0

    if N % 11 == 0:
        e = N

    
    print("#{} ".format(tc, ))

