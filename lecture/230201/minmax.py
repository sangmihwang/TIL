T = int(input())
for t in range(1, T+1):
    N = int(input())
    lis = list(map(int, input().split()))
    maxN = lis[0]
    minN = lis[0]
    for i in range(N):
        if lis[i] > maxN:
            maxN = lis[i]
        if lis[i] < minN:
            minN = lis[i]
    print(f'#{t} {maxN - minN}')
























