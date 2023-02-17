T = int(input())
for t in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    prf = 0                          # 수익

    for i in range(N-2, -1, -1):  # 뒤에서부터 오면서 최댓값 갱신
        if price[i] < price[i + 1]:
            prf += price[i+1] - price[i]
            price[i] = price[i + 1]

    print(f'#{t} {prf}')