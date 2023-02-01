T = int(input())
for t in range(1, T+1):
    N = int(input())          # 5
    mn = 10
    lis = list(map(int, input().split()))    # [5 4 3 2 1]
    count = 0
    for i in range(N):               # 리스트 갯수만큼 반복
        if lis[i] < mn:           #
            mn = lis[i]
            count += 1
        elif lis[i] == mn:
            mn = lis[i]
            continue

    print(f'#{t} ', count)











        #     ans = i
        # print(f'#{t} ', ans)
