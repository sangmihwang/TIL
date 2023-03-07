# i 노드부터 시작하여 bfs 끝까지 돌고 사이클 존재여부를 리턴해주는 함수
def bfs(i):
    iscycle = False
    stack = [i]         # 스택에 푸쉬
    while stack:
        node = stack.pop(0)
        if visited[node] == 1:  # 이미 방문한 곳이면
            iscycle = True
        visited[node] = 1       # 방문처리
        for k in lst[node]:     # 연결된 노드에서
            if visited[k] == 0:      # 방문한 곳이 아니라면
                stack.append(k)
    return iscycle


T = 0
while True:
    T += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    lst = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    # visited가 0인 모든 노드를 돌면서 가능한 모든 연결요소를 순회
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:     # 방문하지 않고
            if not bfs(i):      # 사이클이 아니면
                cnt += 1

    if cnt == 0:
        print(f'Case {T}: No trees.')
    elif cnt == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: A forest of {cnt} trees.')