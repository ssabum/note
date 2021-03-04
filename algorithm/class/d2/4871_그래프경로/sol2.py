# 재귀로 해결
import sys
sys.stdin = open("input.txt")

T = int(input())

def DFS(start):
    # result 변수를 수정해야 하므로
    # visited의 요소 수정은 참조하므로 글로벌 변수 선언x
    global result
    visited[start] = True
    for node in edge_list[start]:
        if not visited[node]:
            if node == G:
                result = 1
                return
            DFS(node)


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    edge_list = [[] for _ in range(V+1)]

    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))

    visited = [False] * (V+1)
    result = 0
    DFS(S)


    print("#{} {}".format(tc, result))

