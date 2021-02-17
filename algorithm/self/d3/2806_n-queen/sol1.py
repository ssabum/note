import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 8 * 8 체스판
    base = [[0 for _ in range(8)] for _ in range(8)]

    kill = 0

    # 64칸에서 한 칸씩 순환하며 잡을 퀸이 있는지 점검
    for x in range(8):
        for y in range(8):
            for i in range(8-x):
                for j in range(8-y):

            

    print(base)

    # print("#{} ".format(tc, ))
