def f(i, k, c):
    global maxV
    if i == k:          # 남은 교환횟수가 없으면
        tmp = int(''.join(card))
        if maxV < tmp:
            maxV = tmp
    else:
        for p in range(c-2):
            for q in range(p+1, c):
                card[p], card[q] = card[q], card[p]
                f(i+1, k, c)

T = int(input())
for t in range(1, T+1):
    num, N = input().split()
    card = list(num)
    N = int(N)
    maxV = 0
    f(0, N, len(card))
    print(f'#{t} {maxV}')