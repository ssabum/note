import sys
sys.stdin = open("input.txt")

T = int(input())

for TC in range(1, T+1):
    P, A, B = map(int, input().split())
    cntA = 0
    cntB = 0
    l = 1
    r = P
    while True:
        c = int((l+r)/2)
        cntA += 1
        if c == A:
            break
        elif c <= A:
            l = c
        else:
            r = c
    l = 1
    r = P
    while True:
        c = int((l+r)/2)
        cntB += 1
        if c == B:
            break
        elif c <= B:
            l = c
        else:
            r = c

    if cntA == cntB:
        print("#{}".format(TC), 0)
    elif cntA > cntB:
        print("#{}".format(TC), 'B')
    else:
        print("#{}".format(TC), 'A')
