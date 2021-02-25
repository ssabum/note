import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0] * len(puzzle[0]))

    result = 0
    cnt = 0

    for r in range(N + 1):
        for c in range(N + 1):
            if puzzle[r][c]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

        for c in range(N + 1):
            if puzzle[c][r]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0

    print('#{} {}'.format(t, result))

