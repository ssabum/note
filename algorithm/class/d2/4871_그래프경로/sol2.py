import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    edge_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int, input().split))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))

    visited =
    
    print("#{} ".format(tc, ))

