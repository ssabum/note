import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    numbers = list(map(int, input().split()))
    tot = 0
    for i in numbers:
        tot += i

    tot = tot / len(numbers)

    tot = int(tot+0.5)

    print("#{} {}".format(tc, tot))
