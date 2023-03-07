T = int(input())
for t in range(1, T +1):
    ans = []
    N = int(input())
    lis = list(map(int, input().split()))
    for i in range(N):
        for n in range(N-1):
            if lis[n]> lis[n+1]:
                lis[n], lis[n+1] = lis[n+1], lis[n]
    
    ans = lis[0]
    for v in range(1, N):
        ans = str(ans) + ' ' + str(lis[v])

 
    print(f'#{t}', ans)
            

