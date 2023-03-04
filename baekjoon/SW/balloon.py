T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for (x, y) in d:
                if 0 <= i+x < N and 0 <= j+y < M:
                    cnt += arr[i+x][j+y]
            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{t} {max_cnt}')