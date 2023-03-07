T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
   
    sum = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni, nj = i + di, j +dj
                if 0 <= ni < N and 0 <= nj < N:
                    s = abs(arr[ni][nj] - arr[i][j])
                    sum += s
    print(f'#{t+1} {sum}')