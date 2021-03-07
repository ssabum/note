import sys
sys.stdin = open("input.txt")

def FindMin(row):
    global my_sum, my_min
    # sum이 min을 넘을 때 버림
    if my_sum > my_min:
        return
    # 마지막 row에 도착할 경우
    if row == N:
        # 기존 결과보다 작다면 갱신
        if my_sum < my_min:
            my_min = my_sum
            return

    for col in range(N):
        # 방문한 적이 없으면
        if not visited[col]:
            # 방문 후 sum증가
            visited[col] = True
            my_sum += my_map[row][col]
            # 다음 row 이동
            FindMin(row + 1)
            # 다음 col로 이동하기 위해 리셋
            my_sum -= my_map[row][col]
            visited[col] = False


T = int(input())
for test_case in range(1, T + 1):
    # N*N 크기, N은 3이상 10미만
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    # 최악의 최소를 고려해서 my_min = N * 9로 설정
    my_sum, my_min = 0, N * 9
    FindMin(0)
    print('#{} {}'.format(test_case, my_min))
