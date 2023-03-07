def BFS(i, j, N):
    visited = [[0] * N for _ in range(N)]   # 방문한 곳 확인용
    queue = [(i, j)]                        # 큐 생성
    visited[i][j] = 1                       # 방문한 곳 1로
    while queue:
        i, j = queue.pop(0)  # 큐의 첫번째 원소 반환
        if miro[i][j] == '3':
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and miro[ni][nj] != '1' and visited[ni][nj] == 0: # 벽 아니고 인큐한 적없으면
                queue.append((ni, nj))
                visited[ni][nj] = 1
    return 0

def start(N):
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                return i, j
    return -1, -1               # 형식 맞추기용

T = int(input())
for t in range(1, T+1):
    N = int(input())
    miro = [input() for _ in range(N)]

    si, sj = start(N)

    print(f'#{t} {BFS(si, sj, N)}')