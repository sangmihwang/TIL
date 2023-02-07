def select(a, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, len(a)):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    return a[k-1]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    new = [0] * N
    m = N
    v = 1
    for n in range(N):
        if n % 2 == 0:
            new[n] = select(num, m)
            m -= 1
        else:
            new[n] = select(num, v)
            v += 1

    new = new[:10]
    print(f'#{t}', *new)