import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    a, b = map(int, input().split())
    quo = a // b
    rem = a % b
    
    print("#{} {} {}".format(tc, quo, rem))

