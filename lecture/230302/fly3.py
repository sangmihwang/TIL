T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    now = (x, y)
    for i in range(N-M+1):
        for j in range(N-M+1):

            kill_d =



