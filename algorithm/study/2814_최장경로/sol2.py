def dfs(graph, start):
    result, visit = [], []
    visit.append(start)

    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])

    return len(result)


# Test Code
graph = dict()
graph[0] = [1, 2]
graph[1] = [0, 3, 4]
graph[2] = [0, 5, 6]
graph[3] = [1]
graph[4] = [1]
graph[5] = [2]
graph[6] = [2]

print(dfs(graph, 0))