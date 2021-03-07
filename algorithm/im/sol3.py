import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M1, M2 = map(int,input().split())
    data = list(map(int,input().split()))

    data.sort(reverse=True)

    result = 0
    idx = 1
    i = 0
    while i < min(M1, M2):
        result += data[i] * idx
        result += data[i+1] * idx
        idx += 1
        i += 2
    while i <= N:


    
    print("#{} ".format(tc, ))

