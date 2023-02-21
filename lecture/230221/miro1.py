def BFS():
    visited = [[0] * 16 for _ in range(16)]   # 방문한 곳 확인용
    queue = [(1, 1)]                        # 큐 생성
    visited[1][1] = 1                       # 방문한 곳 1로
    while queue:
        i, j = queue.pop(0)  # 큐의 첫번째 원소 반환
        if miro[i][j] == '3':
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < 16 and 0 <= nj < 16 and miro[ni][nj] != '1' and visited[ni][nj] == 0: # 벽 아니고 인큐한 적없으면
                queue.append((ni, nj))
                visited[ni][nj] = 1
    return 0

for t in range(1, 11):
    T = int(input())
    miro = [input() for _ in range(16)]

    print(f'#{t} {BFS()}')