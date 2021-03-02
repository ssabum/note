import sys
sys.stdin = open("input.txt")

T = int(input())

def win(x, y):
    if (lst[x-1] == 1 and lst[y-1] == 3) or (lst[x-1] == 1 and lst[y-1] == 1):
        return x
    elif (lst[x-1] == 2 and lst[y-1] == 1) or (lst[x-1] == 2 and lst[y-1] == 2):
        return x
    elif (lst[x-1] == 3 and lst[y-1] == 2) or (lst[x-1] == 3 and lst[y-1] == 3):
        return x
    return y

def match(start, end):
    if start == end:
        return start

    first_value = match(start, (start+end)//2)
    second_value = match((start+end)//2+1, end)
    return win(first_value, second_value)

for tc in range(1, T+1):
    # N: 학생수
    N = int(input())
    # 학생별로 가위바위보 카드, 1=가위, 2=바위, 3=보
    lst = list(map(int, input().split()))
    start = 1
    end = N

    print("#{} {}".format(tc, match(start, end)))
