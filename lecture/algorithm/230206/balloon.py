T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):

        for j in range(M):
            sum = 0
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0], [0,0]]:
                ni, nj = i + di, j +dj
                if 0 <= ni < N and 0 <= nj < M:
                    s = arr[ni][nj]
                    sum += s
            if max_sum < sum:
                max_sum = sum
    print(f'#{t} {max_sum}')

