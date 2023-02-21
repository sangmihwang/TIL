def BFS(S, G):                  # 시작 s, 끝 G
    visited = [0] * (V+1)           # 인큐 확인 배열 (방문한 곳 및 노드 수 확인)
    queue = [S]                   # 큐 생성, 시작점 인큐
    visited[S] = 1                # 시작점 방문지에 표시
    while queue:                  # 큐가 비어있지 않은 경우
        i = queue.pop(0)          # 큐의 첫번째 원소 반환
        if nd[i][G] == 1:
            return visited[i]         # 지나간 노드 수
        for j in range(V+1):
            if nd[i][j] == 1 and visited[j] == 0:    # 연결돼있고 인큐한 적없으면
                queue.append(j)
                visited[j] = visited[i] + 1
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    nd = [[0] * (V+1) for _ in range(V+1)]            # 연결된 노드 표시
    for (i,j) in arr:
        nd[i][j] = 1
        nd[j][i] = 1

    print(f'#{t} {BFS(S, G)}')

