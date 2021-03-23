import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 2이상 1000000이하 자연수. N일 동안 매매가 예측
    # price: N일 동안의 매일매일 매매가, price의 원소 10000이하
    # 하루에 최대 1만큼 구입, 판매는 얼마든 가능
    N = int(input())

    # 뒤에서부터 생각하기 위해 가격을 담아서 거꾸로
    price = list(map(int, input().split()))[::-1]
    
    # 결과 변수
    profit = 0

    # 기준값 설정
    top_price = price[0]
    
    for i in range(1, N):
        # 가격을 순환하면서 기준값이 크면 차액을 이익에 더함
        if top_price > price[i]:
            profit += top_price - price[i]
        # 기준보다 비싼 값이 나오면 기준을 갱신
        else:
            top_price = price[i]

    print("#{} {}".format(tc, profit))

