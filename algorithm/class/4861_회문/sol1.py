import sys
sys.stdin = open("input.txt")

T = int(input())

def palindrome(s):
    # 거꾸로도 같은지 확인하는 함수
    return s == s[::-1]

for tc in range(1, T+1):
    # N: 10이상 100이하, N * N 틀
    # M: 5이상 N이하, 회문길이
    N, M = map(int, input().split())
    # 문자열입력
    str_table_r = [[i for i in input()] for _ in range(N)]
    str_table_l = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            str_table_l[i][j] = str_table_r[j][i]

    result = []

    for i in range(N):
        for j in range(N-M+1):
            if palindrome(str_table_r[i][j:j+M]) == True:
                result.append(str_table_r[i][j:j + M])
            if palindrome(str_table_l[i][j:j+M]) == True:
                result.append(str_table_l[i][j:j + M])

    print("#{} {}".format(tc, "".join(result[0])))