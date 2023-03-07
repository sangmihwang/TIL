def Pas(N):
    arr = [[] for _ in range(N)]
    if N > 1:
        for n in range(2, N):
            arr[n] = [0] * (n+1)
        arr[0] = [1]
        arr[1] = [1, 1]
        for i in range(2, N):
            for j in range(1, i):
                arr[i][0] = 1
                arr[i][-1] = 1
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    elif N == 1:                        # N=1인 경우 빼먹어서 오답
        arr[0] = [1]                    # 행렬에서 인덱스값과 갯수 차이 헷갈림
    return arr

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = Pas(N)

    print(f'#{t}')
    for item in ans:
        print(*item)

