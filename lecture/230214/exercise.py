# 방문 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원)
graph = [
    [],             # 1번 노드와 연결된 노드들
    [2, 3, 8],      # 2번 노드와 연결된 노드들
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def DFS(graph, v, visited):
    visited[v] = True           # 현재 노드를 방문 처리
    print(v, end = ',')
    print(visited)

    for i in graph[v]:
        if not visited:
            DFS(graph, i, visited)
                                # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
DFS(graph, 2, visited)