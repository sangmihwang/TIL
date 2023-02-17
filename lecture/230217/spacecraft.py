def land(arr, N, M):
    di = [-1,0,1]
    dj = [-1,0,1]
    cnt = 0
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            cnt = 0
            for k in range(3):
                for w in range(3):
                    if arr[i+di[k]][j+dj[w]] < arr[i][j]:
                        cnt += 1

            if cnt > 3:
                ans += 1

    return ans


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    gr = [[9]*(M+2)] + [[9] + list(map(int, input().split()))+[9] for _ in range(N)] + [[9]*(M+2)]

    print(f'#{t} {land(gr, N, M)}')

