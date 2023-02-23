N, M = map(int, input().split())
num = list(map(int, input().split()))
mn_dif = 99999
for n in num:
    for m in num:
        for o in num:
            if n != m and m != o and o != n:
                sum = n + m + o
                if sum <= M:
                    dif = M - sum
                    if dif < mn_dif:
                        mn_dif = dif
                        ans = sum
print(ans)



























