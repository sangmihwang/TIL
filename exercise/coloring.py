T = int(input())
for t in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        cnt += ((r2-r1)+(c2-c1)+2)*2

    print(f'#{t} {cnt}')
