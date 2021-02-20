t = 'A patten matching algorithm'
p = "rithm"

def BruteForce(p, t):
    M = len(p)
    N = len(t)
    i = 0
    j = 0

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M
    else : return -1

def BruteForce2(p, t):
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return i
    return -1