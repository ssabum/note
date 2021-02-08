import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    if m1 == m2:
        result = d2 - d1 + 1


    
    print("#{} ".format(tc, ))

