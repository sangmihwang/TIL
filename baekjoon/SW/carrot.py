T = int(input())
for t in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    s = []
    m = []
    l = []
    for a in range(1, N-2):
        for b in range(a+1, N-1):
            for i in range(a):
                s.append(Ci[i])
            for i in range(b):
                m.append(Ci[i])
            for i in range()

    print(f'#{t}')