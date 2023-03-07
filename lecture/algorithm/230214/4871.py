def f1(S, G, N):  # 그래프 탐색 # S는 출발, G는 도착, N은 마지막 정점
    visited = [0] * (N + 1)  # 방문표시
    stack = []  # 스택
    v = S  # 출발점
    while True:
        # print(v) # v에 방문했을 때 확인하고 싶으면
        if v == G:  # 혹시 v가 목적지라면 ?
            return 1  # 방문해서 목적지까지 갔으면 성공 !!!
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
    # return visited[G]   # 탐색 중에 G를 거쳐갔다면 ?? visited[G] == 1 이다
    return 0  # 실패 v==G인지 검사했는데 아닌거임..


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]  # 간선, 인접행렬
    # adjL = [[] for _ in range(V+1)]
    for i in range(E):  # 간선의 수만큼 들어온다
        v, w = map(int, input().split())  # v 출발, w 도착
        adjM[v][w] = 1  # v와 w는 인접해 있다 라는 뜻. v > w 방향임
        # G[w][v] = 1 # 방향이 없다면 추가해줬어야함, 무향그래프
    S, G = map(int, input().split())  # s는 출발 g는 도착 (경로존재확인)
    print(f'#{tc} {f1(S, G, V)}')