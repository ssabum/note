import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N * N 행렬
    N = int(input())
    # 입력 숫자들 하난씩 담기
    data = []
    for _ in range(N):
        num = list(map(int,input().split()))
        for i in num:
            data.append(i)

    # 결과담을 리스트
    # 이렇게 하면 같은 리시트를 참고하게 되서 한꺼번에 저장
    # ans_1 = [[0] * N] * N
    ans_1 = [[0 for _ in range(N)] for _ in range(N)]

    idx = 0
    breaker = True
    while True:
        for i in range(N-1, -1, -1):
            for j in range(N):
                ans_1[j][i] = data[idx]
                if idx == (N ** 2)-1:
                    breaker = False
                    break
                idx += 1
            if breaker == False:
                break
        if breaker == False:
            break

    # 두번째 회전
    ans_2 = [[0 for _ in range(N)] for _ in range(N)]

    idx = 0
    breaker = True
    while True:
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                ans_2[i][j] = data[idx]
                if idx == (N ** 2)-1:
                    breaker = False
                    break
                idx += 1
            if breaker == False:
                break
        if breaker == False:
            break

    # 세번째 회전
    ans_3 = [[0 for _ in range(N)] for _ in range(N)]

    idx = 0
    breaker = True
    while True:
        for i in range(N):
            for j in range(N-1, -1, -1):
                ans_3[j][i] = data[idx]
                if idx == (N ** 2)-1:
                    breaker = False
                    break
                idx += 1
            if breaker == False:
                break
        if breaker == False:
            break

    print("#{}".format(tc))
    for i in range(N):
        for j in ans_1[i]:
            print(j, end="")
        print(" ", end="")
        for j in ans_2[i]:
            print(j, end="")
        print(" ", end="")
        for j in ans_3[i]:
            print(j, end="")
        print(" ", end="")
        print()

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    
    print("#{} ".format(tc, ))

