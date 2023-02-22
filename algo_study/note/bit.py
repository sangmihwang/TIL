i = 1 << 8        # 256
i = i >> 1      # 128
print(i)


## 숫자 조합

N, M = 8, 3
for i in range(1 << N):
    cnt = 0
    res = []
    while i:
        if i & 1:
            res.append(cnt + 1)
        cnt += 1
        i = i >> 1
    if len(res) == M:
        print(*res)