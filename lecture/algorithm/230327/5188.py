
## 5188 _ 최소합

def f(i, k):
    global x, y, minV
    x = 0
    y = 0
    sum = arr[x][y]

    if i == k:
        for pi in p:
            if pi == 0:         # 오른쪽으로
                y += 1
                sum += arr[x][y]
            else:               # 아래로
                x += 1
                sum += arr[x][y]
        if sum < minV:
            minV = sum

    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = di[j]
                used[j] = 1
                f(i+1, k)
                used[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0]*(N-1) + [1]*(N-1)
    p = [0]*(2*(N-1))
    used = [0]*(2*(N-1))
    minV = 9999
    f(0, 2 * (N - 1))

    print(f'#{t} {minV}')