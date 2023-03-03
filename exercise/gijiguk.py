T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [['X']*(N+2)] + [['X']+list(input())+['X'] for _ in range(N)] + [['X']*(N+2)]
    d = [('A', 1), ('B', 2), ('C', 3)]

    for (x, k) in d:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if arr[i][j] == x:
                    for l in range(1, k+1):
                        if arr[i-l][j] == 'H':      # 상
                            arr[i-l][j] = 'X'
                        if arr[i][j-l] == 'H':      # 좌
                            arr[i][j-l] = 'X'
                        if arr[i][j+l] == 'H':      # 우
                            arr[i][j+l] = 'X'
                        if arr[i+l][j] == 'H':      # 하
                            arr[i+l][j] = 'X'
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'{t} {cnt}')



