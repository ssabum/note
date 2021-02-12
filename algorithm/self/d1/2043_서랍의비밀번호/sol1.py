import sys
sys.stdin = open("input.txt")

P, K = map(int, input().split())

cnt = 1

if P == K:
    print(cnt)

while P != K:
    if K == 999:
        K = 0
    K += 1
    cnt += 1
    if P == K:
        print(cnt)



