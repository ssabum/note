# 실패작...
import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(graph, start):
    result, visit = [], []
    visit.append(start)

    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])

    return len(result)

# 최장 경로 길이: 정점의 개수!!
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # 인접리스트 딕셔너리
    # 결과변수
    dict = {}
    # for i in range(1, N+1):
    #     dict[i] = []

    result = 0
    # 간선이 0개 일때는 1을 출력
    if M == 0:
        result = 1
    # 입력값을 반복하면서 dict에 추가
    for _ in range(M):
        a, b = input().split()
        # 만약 key가 존재하면 value에 추가
        if a in dict:
            dict[a].append(b)
            dict[b].append(a)
        # key가 없으면 value 생성
        else:
            dict[a] = [b]
            dict[b] = [a]
            # dict

    print(dict)

    # # 최장거리 갱신 변수
    # maxx = 0
    # # 시작점을 key들로 순환하면서 최장거리 체크
    # for i in dict.keys():
    #     if maxx < dfs(dict, i):
    #         maxx = dfs(dict, i)
    # result = maxx
    #
    # print("#{} {}".format(tc, result))