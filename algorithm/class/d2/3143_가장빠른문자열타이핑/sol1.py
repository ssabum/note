import sys
sys.stdin = open("input.txt")

T = int(input())

def bruteforce(B, A):
    i, j = 0, 0
    a = len(A)
    b = len(B)
    cnt = 0
    while j < b and i < a:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == b : cnt += 1
    return cnt

for tc in range(1, T+1):
    A, B = map(input().split())

    bruteforce(B, A)



    # print("#{} ".format(tc, ))

