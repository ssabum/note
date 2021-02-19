import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N: 찾는 문자열
    n = input()
    n_size = len(n)
    # M: 전체 문자열
    m = input()
    m_size = len(m)

    max = 0

    for i in n:
        tot = 0
        for j in m:
            if i == j:
                tot += 1
        if tot > max:
            max = tot
    
    print("#{} {}".format(tc, max))

