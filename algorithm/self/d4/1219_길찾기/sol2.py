# 인접행렬
import sys
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc, E = list(map(int, input().split()))
    edge_input = list(map(int, input().split()))

    edge_matrix = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(E):
        start_node = edge_input[i*2]
        end_node = edge_input[i*2+1]
        edge_matrix[start_node][end_node] = 1

    visited = [False] * 100
    stack = [0]

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True
            for v in range(100):
                if not visited[v] and edge_matrix[now][v] == 1:
                    stack.append(v)

    result = 1 if visited[99] else 0

    print("#{} {}".format(tc, result))

