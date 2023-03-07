def sol(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    elif N > 20:
        return sol(N-10) + 2*sol(N-20)


T = int(input())
for t in range(1, T+1):
    N = int(input())

    print(f'#{t} {sol(N)}')

