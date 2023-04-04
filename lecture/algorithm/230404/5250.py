
## 5250 SWEA 최소 비용

def f(N):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = [(0,0)]
    while q:
        (i, j) = q.pop(0)
        for n in range(4):
            if 0 <= i+di[n] <N and 0<=j+dj[n] <N:       # 판 안 벗어나야
                plus = cons[i][j] + 1 + (arr[i+di[n]][j+dj[n]] - arr[i][j] if arr[i+di[n]][j+dj[n]] >= arr[i][j] else 0)
                if cons[i+di[n]][j+dj[n]] > plus:
                    cons[i + di[n]][j + dj[n]] = plus

                    q.append((i + di[n], j + dj[n]))

    return cons[N-1][N-1]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000000
    cons = [[INF]*N for _ in range(N)]
    cons[0][0] = 0
    i = j = 0       # (0, 0)에서 출발

    print(f'#{t} {f(N)}')