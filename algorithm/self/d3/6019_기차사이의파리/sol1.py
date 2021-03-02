import sys
sys.stdin = open("input.txt")

T = int(input())

def fly(d, a, b, f):
    return (d / (a+b)) * f

for tc in range(1, T+1):
    # D: 기차 사이 거리
    # A, B: 두 기차의 속력
    # F: 파리의 속력
    D, A, B, F = list(map(int, input().split()))
    result = fly(D, A, B, F)
    
    print("#{} {}".format(tc, result))