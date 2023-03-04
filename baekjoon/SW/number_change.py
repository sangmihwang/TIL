def max_N(N):
    maxnum = 0
    if N[0] == max(N):
        for i in range(1, len(N)):
            if N[i] > maxnum:
                maxnum
                N[0], N[i] = N[i], N[0]
    else:
        for i in range(len(N)):
            if N[i] == max(N):
                N[0], N[i] = N[i], N[0]
    str1 = ''
    for a in N:
        str1 += str(a)
    return int(str1)

def min_N(N):
    for i in range(len(N)):
        if N[i] == min(N):
            N[0], N[i] = N[i], N[0]

    str2 = ''
    for a in N:
        str2 += str(a)
    return int(str2)

T = int(input())
for t in range(1, T+1):
    N = list(map(int, input()))

    print(f'#{t} {min_N(N)} {max_N(N)}')
