T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                for a in [arr[j]]:
                    print(a)
    #                 sum += int(a)
    #             if sum == K:
    #                 ans = j
    #
    # print(f'#{t} {ans}')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    cnt = 0

    for i in range(1 << 12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])
                sum_v += arr[j]
        if len(subset) == N and sum_v == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))