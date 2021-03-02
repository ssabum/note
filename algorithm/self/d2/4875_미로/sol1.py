import sys
sys.stdin = open("input.txt")

T = int(input())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

for tc in range(1, T+1):
    # N: 미로 크기
    N = int(input())
    miro = [[int(i) for i in input()] for _ in range(N)]
    y, x, result = 0, 0, 0
    # 시작점 찾기
    for i in range(N):
        if 2 in miro[i]:
            x = miro[i].index(2)
            y = i
            break
    # 스택에 시작 위치 추가
    stack = [(y, x)]
    # 스택이 빌때까지 반복
    while stack:
        temp = []
        # 스택에 있는 위치를 꺼내서
        y, x = stack.pop()
        # 현재 위치는 갔다고 변경
        miro[y][x] = 1
        # 이동할 방향 검사
        for c, r in move:
            dy = y+c
            dx = x+r
            # 가는 길이 테두리를 벗어나면 다음길로
            if iswall(dy, dx):
                continue
            # 가는 길이 3이면 도착
            if miro[dy][dx] == 3:
                result = 1
                break
            # 0이라면 갈 수 있는 장소를 스택에 추가
            elif not miro[dy][dx]:
                stack.append((dy, dx))
        else:
            # 브레이크 없이 끝났으면 다음것으로 반복
            continue
        # 브레이크문으로 여기까지 왔다면 반복 멈추기
        break
    # 결과 출력
    print("#{} {}".format(tc, result))