def f1(S, G, N):    # S는 출발, G는 도착, N은 마지막 정점
    visited = [0] * (N+1)     # 방문표시
    stack = []          # 스택
    v = S               # 출발점
    while True:
        if v == G:          # 혹시 v가 목적지
            return 1        # 방문해서 목적지까지 갔으면 성공
        visited[v] = 1
        for w in range(1, N + 1):
            if adjM[v][w] and visited[w] == 0:  # 인접하고 방문안한 w가 있으면 !
                stack.append(v)  # 이동하기전에 현재정점을 넣어놔라
                v = w  # v 에서 w로 이동해봐
                break  # 갈 곳을 찾았다면 이제 이동했으니까 거기서부터 (w)에서 가야함
        else:  # 인접 정점이 없으면 !! 다시 빽해서 탐색해야하니까
            if stack:  # stack에 뭐가 있다면 [1,3> 3에서 아무것도없으면]
                v = stack.pop()
            else:  # 스택이 비어있으면
                break

    return 0


for t in range(1, 11):
    T, R = map(int, input().split())       # 테스트 케이스와 길의 개수
    arr = list(map(int, input().split()))   # 길의 순서쌍
    adjM = [[0] * (101) for _ in range(101)]

    for i in range(R):
        v1, v2 = arr[i*2], arr[i*2 + 1]
        adjM[v1][v2] = 1













#
# def dfs(graph, v, visited):
#     visited[v] = True
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#
# for tc in range(1, 11):
#     T, E = map(int, input().split())
#
#     e_li = list(map(int, input().split()))
#
#     graph_lst = [[] for _ in range(101)]
#
#     visited = [False] * len(graph_lst)
#
#     for j in range(0, E):
#         v1, v2 = e_li[j * 2], e_li[j * 2 + 1]
#         graph_lst[v1].append(v2)
#
#     dfs(graph_lst, 0, visited)
#
#     if visited[99]:
#         print(f'#{tc} {1}')
#     else:
#         print(f'#{tc} {0}')
