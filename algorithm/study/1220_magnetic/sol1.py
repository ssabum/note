import sys
sys.stdin = open("input.txt")

# 최대한 단순하게 생각하기!!!
for tc in range(1, 11):
    # bord 크기
    N = int(input())
    # 입력값 받아오기
    bord = [list(map(int, input().split())) for _ in range(N)]
    # 결과변수
    result = 0
    # y축으로 반복
    for j in range(N):
        tmp = []
        # 만약이면 1이면 스택에 저장
        for i in range(N):
            if bord[i][j] == 1:
                tmp.append(1)
            # 스택에 1이 있는 상태에서 2를 만나면 교착발생
            if bord[i][j] == 2 and tmp:
                result += 1
                # 스택초기화
                tmp.clear()
    # 결과출력
    print("#{} {}".format(tc, result))

