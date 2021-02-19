import sys
sys.stdin = open("input.txt")

def palindrome(s):
    # 거꾸로도 같은지 확인하는 함수
    return s == s[::-1]

for _ in range(1, 11):
    num = int(input())
    str_table_r = [[i for i in input()] for _ in range(100)]
    str_table_l = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            str_table_l[i][j] = str_table_r[j][i]

    result = []
    flag = True

    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(100-k+1):
                if palindrome(str_table_r[i][j:j+k]) == True:
                    result.append(k)
                if palindrome(str_table_l[i][j:j+k]) == True:
                    result.append(k)
                if len(result) > 0:
                    flag = False
                    break
        if flag == False:
            break

    print("#{} {}".format(num, result[0]))

