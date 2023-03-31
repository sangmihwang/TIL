
## SWEA 등산로 조성

def dfs(n, i, j, cnt):       # 시작점 높이, 시작점 좌표(i,j)
    global flag
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    if n == minH:
        for (di, dj) in d:
            if 0 <= i + di < N and 0 <= j + dj < N:
                if n == arr[i + di][j + dj]:
                    cnt += 1
        cnt_lst.append(cnt)
        return


    for (di, dj) in d:
        if 0 <= i+di < N and 0 <= j+dj < N:     # 지도 안 범위면
            if n > arr[i+di][j+dj]:             # 높이 낮으면 옮겨가라
                dfs(arr[i+di][j+dj], i+di, j+dj, cnt+1)
            elif n == arr[i+di][j+dj]:
                if flag == 0:
                    flag = 1
                dfs(arr[i+di][j+dj]-1, i+di, j+dj, cnt+1)

    cnt_lst.append(cnt)
    return


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())    # N 지도 한 변의 길이, K 공사 가능 깊이
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxH = 0
    minH = 21
    flag = 0
    ij_lst = []             # 최고점 좌표 리스트
    cnt_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= maxH:
                maxH = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= minH:
                minH = arr[i][j]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == maxH:
                cnt = 0
                dfs(maxH, i, j, 0)

    print(f'#{t} {max(cnt_lst)}')