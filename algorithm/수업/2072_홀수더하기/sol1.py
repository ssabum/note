import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    numbers = list(map(int, input().split()))

    tot = 0

    for i in numbers:
        if i % 2:
            tot += i

    print("#{} {}".format(tc, tot))

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    
    print("#{} ".format(tc, ))

