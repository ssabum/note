import sys
sys.stdin = open("input.txt")

T = int(input())

def num_change(str, n):
    i = 0
    tot = []
    while i < n:
        for i in range(len(str)):


        i += 1

for tc in range(1, T+1):
    # digit: 숫자판 정보, 최대 6자리
    # change: 교환 횟수, 최대 10
    digit, change =  map(int, input().split())
    digit = str(digit)
    # 최대 상금
    max_money = 0
    # 상금 담을 리스트
    money = []


    # 최대 상금 추출을 위한 버블정렬
    # for i in range(len(money)-1, 0, -1):
    #     for j in range(0, i):
    #         if money[j] > money[j+1]:
    #             money[j], money[j+1] = money[j+1], money[j]
    #
    # print("#{} {}".format(tc, max_money[-1]))

