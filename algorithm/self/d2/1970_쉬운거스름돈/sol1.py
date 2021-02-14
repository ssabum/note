import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 10이상 1000000이하 정수, 마지막 자릿수는 항상 0
    N = input()
    N = N[:len(N)-1]+"0"
    N = int(N)

    # 결과 담을 리스트
    result = [0 for _ in range(8)]

    # 5만원 거스름돈
    while N // 50000:
        result[0] = N // 50000
        N = N % 50000
    # 1만원 거스름돈
    while N // 10000:
        result[1] = N // 10000
        N = N % 10000
    # 5천원 거스름돈
    while N // 5000:
        result[2] = N // 5000
        N = N % 5000
    # 1천원 거스름돈
    while N // 1000:
        result[3] = N // 1000
        N = N % 1000
    # 5백원 거스름돈
    while N // 500:
        result[4] = N // 500
        N = N % 500
    # 1백원 거스름돈
    while N // 100:
        result[5] = N // 100
        N = N % 100
    # 5십원 거스름돈
    while N // 50:
        result[6] = N // 50
        N = N % 50
    # 1십원 거스름돈
    while N // 10:
        result[7] = N // 10
        N = N % 10

    print("#{} ".format(tc))
    for i in result:
        print(i, end=" ")
    print()

