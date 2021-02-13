import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # N은 5이상 15이하의 정수
    # K는 2이상 N이하의 정수
    N, K = map(int, input().split())

    # 전체 퍼즐 담을 리스트
    puzzle = []
    # 각 행마다 입력받아서 전체 퍼즐 리스트에 저장
    for i in range(N):
        data = list(map(int, input().split())) + [0]
        puzzle.append(data)
    puzzle.append([0] * (N+1))

    # 맞을 경우
    match = 0
    # 맞을 경유의 합
    cnt = 0
    # 가로줄에 들어갈 경우 / 가로로 순환
    for i in range(N):
        for j in range(N):
            # 0이면 match 리셋
            if puzzle[i][j] == 0:
                match = 0
            # 1이면 match += 1
            else:
                match += 1
                # match와 k수 같아지고 다음칸에 0이면
                if match == K and puzzle[i][j+1] == 0:
                    # cnt += 1
                    cnt += 1

    # 세로줄에 들어갈 경우 / 세로로 순환
    for i in range(N):
        for j in range(N):
            if puzzle[j][i] == 0:
                match = 0
            else:
                match += 1
                if match == K and puzzle[j+1][i] == 0:
                    cnt += 1

    print("#{} {}".format(tc, cnt))

