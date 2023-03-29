
## 5188 _ 최소합

def f(i, j, k, s):
    global minV
    if i >= k or j >= k:
        return
    elif i == k-1 and j == k-1:
        if s+arr[i][j] < minV:  # 도착지점 값 더해줘야
            minV = s+arr[i][j]
    else:
        f(i+1, j, k, s+arr[i][j])
        f(i, j+1, k, s+arr[i][j])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*(N) for _ in range(N)]
    minV = 9999

    f(0, 0, N, 0)

    print(f'#{t} {minV}')