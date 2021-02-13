import sys
sys.stdin = open("input.txt")

P, K = map(int, input().split())

count = 1

if P == K:
    print(count)

while P != K:
    if K == 999:
        K = 0
    K += 1
    count += 1
    if P == K:
        print(count)



