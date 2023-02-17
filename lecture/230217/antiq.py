def mon(N, M, ant):
    max_cnt = 0
    for i in range(N):
        cnt = 0                         # 새로운 줄 시작할 때
        for j in range(M):
            if ant[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0                 # 한 줄 내에서 1 나오다가 0 나오면
    return max_cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ant = [list(map(int, input().split())) for _ in range(N)]   # 가로 M 세로 N
    ant_r = [[0]*N for _ in range(M)]           # 가로 N 세로 M

    for i in range(M):
        for j in range(N):
            ant_r[i][j] = ant[j][i]

    ans = max(mon(N, M, ant), mon(M, N, ant_r))

    print(f'#{t} {ans}')
