def BFS(i, j, N):
    visited = [[0]*N for _ in range(N)]     # 인큐 확인 배열 (방문한 곳 및 칸 수 확인)
    queue = [(i, j)]                # 큐 생성, 시작점 인큐
    visited[i][j] = 1               # 시작점 방문지에 표시
    while queue:                    # 큐가 비어있지 않은 경우
        i, j = queue.pop(0)          # 큐의 첫번째 원소 반환
        if miro[i][j] == '3':
            return visited[i][j] - 2        # 지나간 칸 수에서 시작과 끝칸 뺌
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and miro[ni][nj] != '1' and visited[ni][nj] == 0: # 벽 아니고 인큐한 적없으면
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0                # '3'칸에 못 가는 경우

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

