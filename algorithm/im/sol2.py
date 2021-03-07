import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M1, M2 = map(int,input().split())
    M_list = list(map(int,input().split()))

    sorted_reversed_M = sorted(M_list)[::-1] # [7, 5, 4, 3, 1]

    M1_list = []
    M2_list = []

    for i in range(len(sorted_reversed_M)):
        if i == 0 or i % 2 == 0 :
            M1_list += [sorted_reversed_M[i]]
        else:
            M2_list += [sorted_reversed_M[i]]
    # print(M1_list) # [5, 3]
    # print(M2_list) # [7, 4, 1]


    if M1 < len(M1_list):
        M2_list += M1_list[M1:]
        M2_list.sort(reverse=True)
        M1_list = M1_list[:M1]

    if M2 < len(M2_list): # = M1 > len(M1_list)
        M1_list += M2_list[M2:]
        M1_list.sort(reverse=True)
        M2_list = M2_list[:M2]

    # print(M1_list, M2_list)

    result_1, result_2 = 0, 0

    for i in range(len(M1_list)) :
        result_1 += (i+1)*M1_list[i]
    for j in range(len(M2_list)):
        result_2 += (j+1)*M2_list[j]

    result = result_1 + result_2

    print(result)