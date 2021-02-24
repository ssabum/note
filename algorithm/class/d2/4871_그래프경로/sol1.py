import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # V: 노드, E: 간선
    V, E = list(map(int, input().split()))

    # 인접행렬
    # edge_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    # for _ in range(E):
    #     start_node, end_node = list(map(int, input().split()))
    #     edge_matrix[start_node][end_node] = 1
    # S, G = list(map(int, input().split()))

    # 인접리스트
    edge_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    # 출발, 도착 노드
    S, G = list(map(int, input().split()))

    # 방문 리스트
    visited = [False for _ in range(V+1)]
    # visited = [False] * (V+1)
    # 스택
    stack = [S]

    # 스택에 원소가 있으면 반복
    while stack:
        # 현재 위치
        now = stack.pop()
        # 현재 위치에 방문 했다면
        if not visited[now]:
            # 방문 안 했다면
            visited[now] = True
        # 현재 위치의 노드에 연결된 노드들 반복
        for v in edge_list[now]:
            # 방문 안한 노드면
            if not visited[v]:
                stack.append(v)

    # 출발, 도착 노드의 경로 확인
    result = 1 if visited[G] else 0

    print("#{} {}".format(tc, result))