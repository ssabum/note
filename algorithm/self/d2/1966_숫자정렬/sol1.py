import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 5이상 50이하 숫자의 개수
    # number는 입력 숫자값
    N = int(input())
    number = list(map(int, input().split()))
    
    # 버블정렬
    for i in range(len(number)-1, 0, -1):
        for j in range(0, i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]

    # 문제에서 요구하는 형식에 맞게 출력
    print("#{} ".format(tc), end="")

    for i in number:
        print(i, end=" ")

    print()

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    
    print("#{} ".format(tc, ))

