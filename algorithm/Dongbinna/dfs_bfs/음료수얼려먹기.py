# 연결 요소 찾기 문제(connected component)
n, m = map(int, input().split())
# 2차원 리스트 맵 정보 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m: return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치들 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs수행, 이때 처음 방문이 경우에만 카운트 증가
        if dfs(i, j) == True:
            result += 1

print(result)