
## N - Queen 백트래킹
# 체스판을 채워보는 방법

def promising(i, j):

    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        while 0 <=ni <N and 0 <=nj <N:         # 판을 벗어나지 않게
            if board[ni][nj]:       # 다른 퀸이 있으면
                return 0            # 실패
            ni, nj = ni+di, nj+dj
    return 1                # i, j에 퀸 놓을 수 있음

def f(i, N):
    global cnt
    global c
    c += 1
    if i == N:      # N개의 퀸을 놓는 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i,j):
                board[i][j] = 1
                f(i+1, N)
                board[i][j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]
    cnt = 0
    c = 0
    f(0, N)
    print(f'#{t} {cnt}')