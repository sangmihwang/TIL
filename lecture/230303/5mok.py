def solve(arr, N):
    for i in range(N):                  # (0,1) 방향
        for j in range(N-5+1):
            cnt = 0
            if arr[i][j] == 'o':
                for k in range(5):
                    if arr[i][j+k] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                if cnt >= 5:
                    return 'YES'
    for j in range(N):                  # (1,0) 방향
        for i in range(N-5+1):
            cnt = 0
            if arr[i][j] == 'o':
                for k in range(5):
                    if arr[i+k][j] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                if cnt >= 5:
                    return 'YES'
    for i in range(N-5+1):                  # (1,1) 방향
        for j in range(N-5+1):
            cnt = 0
            if arr[i][j] == 'o':
                for k in range(5):
                    if arr[i+k][j+k] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                if cnt >= 5:
                    return 'YES'
    for i in range(4, N):                  # (-1,1) 방향
        for j in range(N-5+1):
            cnt = 0
            if arr[i][j] == 'o':
                for k in range(5):
                    if arr[i-k][j+k] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                if cnt >= 5:
                    return 'YES'

    return 'NO'

T = int(input())
for t in range(1, T+1):             # 한 방향으로만 찾으면 된다!(-1,1)(0,1)(1,1)(1,0)
    N = int(input())
    arr = [list(i for i in input()) for _ in range(N)]

    print(f'#{t} {solve(arr, N)}')


