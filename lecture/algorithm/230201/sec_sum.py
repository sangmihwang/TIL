T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    lis = list(map(int, input().split()))

    maxV = 0
    minV = 1000000

    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += lis[j]

        if maxV < s:
            maxV = s
        if minV > s:
            minV = s
    print(f'#{t} {maxV - minV}')
