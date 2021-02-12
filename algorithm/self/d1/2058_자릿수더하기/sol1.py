import sys
sys.stdin = open("input.txt")

T = int(input())

tot = 0

while T % 10:
    i = T % 10
    tot += i
    T = T // 10

print(tot)

