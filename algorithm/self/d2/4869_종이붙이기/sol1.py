import sys
sys.stdin = open("input.txt")

# 팩토리얼 함수
def fa(n):
    if n > 1:
        return n * fa(n-1)
    else:
        return 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # [10 사각형의 개수, 20 사각형의 개수] 모든 조합
    sets = []
    # 중간에 팩토리얼 한 값 저장할 곳
    case = 0
    # 최종 결과
    ans = 0

    for i in range(N//10 + 1):
        for j in range(N//20 + 1):
            if 10*i + 20*j == N:
                sets.append([i, j])
    #[[1, 1], [3, 0]]
    # [[1, 2], [3, 1], [5, 0]]
    # [[1, 3], [3, 2], [5, 1], [7, 0]]

    # 이제 집합들을 하나씩 꺼내서 몇 가지가 가능하지 판단한다.
    for s in sets:
        # 먼저 10 한 가지로 다 채우는 경우
        if s[1] == 0:
            ans += 1
        # 10, 20 둘 다 사용하는 경우
        if s[1] > 0 and s[0] > 0:
            # 20과 10의 위치를 바꾸는 경우
            case += fa(sum(s))//(fa(s[0])*fa(s[1]))
            # 20을 10의 가로로 나눌 경우
            ans += case * (2**s[1])
            case = 0
        # 20만 들어있는 경우
        if s[0] == 0:
            ans += 2**s[1]

    print("#{} {}".format(tc, ans))