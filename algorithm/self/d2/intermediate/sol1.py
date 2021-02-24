import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N * N 크기, N은 50이하 숫자
    N = int(input())
    data = [[i for i in input()] for _ in range(N)]
    # H: 집, A, B, C: 1, 2, 3개 커버 기지국
    # 집 위치를 x,y좌표로 받는 2차원 리스트
    home = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == "H":
                home.extend([i,j])
    # 집마다 확인 반복 횟수
    idx = 0
    # 와이파이 안터지는 집 숫자
    result = 0
    # 델타 이용 리스트 위에서부터 시계방향 / 앞에 0을 넣어준 이유는 뒤에 등장
    row = [0, -1, 0, 1, 0]
    col = [0, 0, 1, 0, -1]
    alph = ["0", "A", "B", "C"]
    while idx < len(home):
        # 집의 x, y 좌표
        x, y = home[idx]
        # 와이파이 터지는지 안터지는지 확인, 초기값 false
        ans = False
        # i의 숫자를 증가시켜가며 델타 인덱스와 주파수 터지는 범위를 설정
        for i in range(1, 4):
            # 아까 리스트 맨앞에 0을 넣어준 이유는 여기서 기지국마다 길이가 1씩 증가하니 이를 표현하기 위해서
            row = [i * j for j in row]
            col = [i * j for j in col]
            # 만약 터지면 true저장 후 종료
            if data[x+row[i]][y+col[i]] == alph[i]:
                ans = True
                break
        # 만약 상하좌우 다 확인해도 false면 와이파이 안터지는 집 카운트 증가
        if ans == False:
            result += 1
        idx += 1

    print("#{} {}".format(tc, result))