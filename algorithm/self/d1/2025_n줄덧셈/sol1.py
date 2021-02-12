import sys
sys.stdin = open("input.txt")

T = int(input())

tot = 0

for i in range(1, T+1):
    tot += i

print(tot)