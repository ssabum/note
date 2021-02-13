import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # P: A사의 1L당 요금
    # Q: B사의 기본 요금
    # R: B사 초과 기준
    # S: B사 초과량에 대해 1L당 요금
    # W: 한달간 사용하는 수도량
    # 모든 수는 1이상 10000이하 자연수
    P, Q, R, S, W = map(int, input().split())

    # a회사, b회사, 저렴한 요금
    ans_a = 0
    ans_b = 0
    ans = 0

    # a회사 요금
    ans_a = W * P

    # b회사 요금
    if W > R:
        ans_b = Q + S * (W-R)
    else:
        ans_b = Q

    # 두 회사에서 뭐가 더 싼지
    if ans_a >= ans_b:
        ans = ans_b
    else:
        ans = ans_a

    print("#{} {}".format(tc, ans))

