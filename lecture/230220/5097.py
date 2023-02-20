T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for i in range(M):
        Q.append(Q.pop(0))
    print(f'#{t} {Q[0]}')

