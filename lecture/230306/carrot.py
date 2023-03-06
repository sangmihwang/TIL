def carrot(N, Ci):
    dif = 1000
    ans = -1
    for a in range(1, N - 1):           # 첫번째 경계 a
        for b in range(a + 1, N):       # 두번째 경계 b
            s = Ci[:a]
            m = Ci[a:b]
            l = Ci[b:]

            if len(s) <= len(Ci) // 2 and len(m) <= len(Ci) // 2 and len(l) <= len(Ci) // 2:
                if s[-1] != m[0] and m[-1] != l[0]:
                    if max(len(s), len(m), len(l)) - min(len(s), len(m), len(l)) < dif:
                        dif = max(len(s), len(m), len(l)) - min(len(s), len(m), len(l))
                        ans = dif
    return ans

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()

    print(f'#{t} {carrot(N, Ci)}')


