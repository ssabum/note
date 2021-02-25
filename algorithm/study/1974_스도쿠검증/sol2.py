import sys
sys.stdin = open("input.txt")

T = int(input())

def check():
    # 가로 검사
    for r in range(9):
        if len(set(bord[r])) != 9:
            return 0
    # 세로 검사
    for c in range(9):
        tmp = set()
        for r in range(9):
            tmp.add(bord[r][c])
        if len(tmp) != 9:   
            return 0
    # 작은 사각형 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = set()
            for r in range(3):
                for c in range(3):
                    tmp.add(bord[i+r][j+c])
            if len(tmp) != 9:
                return 0
    return 1

for tc in range(1, T+1):
    bord = [input().split() for _ in range(9)]
    print("#{} {}".format(tc, check()))

