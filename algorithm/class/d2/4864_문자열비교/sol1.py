import sys
sys.stdin = open("input.txt")

T = int(input())

def bruteforce(N, M):
    i, j = 0, 0
    while j < n and i < m:
        if M[i] != N[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == n : return 1
    else : return 0

for tc in range(1, T+1):
    # N: 찾는 문자열
    N = input()
    n = len(N)
    # M: 전체 문자열
    M = input()
    m = len(M)

    result = bruteforce(N, M)

    print("#{} {}".format(tc, result))

