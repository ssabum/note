import sys
sys.stdin = open("input.txt")

T = int(input())

# 카드 한덱 전부가 필요
# S,D,H,C순서로 몇 장이 더 필요한지 출력
for tc in range(1, T+1):
    # S는 TXY순서로 반복
    # T: 카드무늬(S,D,H,C)
    # XY: 카드 숫자, 01~13
    S = input()

    s_list = [0 for _ in range(1, 14)]
    d_list = [0 for _ in range(1, 14)]
    h_list = [0 for _ in range(1, 14)]
    c_list = [0 for _ in range(1, 14)]

    my_list = [] # ['S01', 'D02', 'H03', 'H04']
    for i in range(0,len(S),3):
        my_list.append(S[i:i+3])

    for i in range(len(my_list)):
        if my_list[i][:1] == "S":
            s_list[int(my_list[i][1:])-1] += 1
        if my_list[i][:1] == "D":
            d_list[int(my_list[i][1:])-1] += 1
        if my_list[i][:1] == "H":
            h_list[int(my_list[i][1:])-1] += 1
        if my_list[i][:1] == "C":
            c_list[int(my_list[i][1:])-1] += 1

    res = ""
    for i in range(len(s_list)):
        if s_list[i] > 1 or d_list[i] > 1 or h_list[i] > 1 or c_list[i] > 1:
           res = "ERROR"

    s_cnt, d_cnt, h_cnt, c_cnt = 0, 0, 0, 0
    for i in range(len(s_list)):
        if s_list[i] == 0:
            s_cnt += 1
        if d_list[i] == 0:
            d_cnt += 1
        if h_list[i] == 0:
            h_cnt += 1
        if c_list[i] == 0:
            c_cnt += 1

    if not res == "ERROR":
        print("#{} {} {} {} {}".format(tc, s_cnt, d_cnt, h_cnt, c_cnt))
    else:
        print("#{} {}".format(tc, res))

