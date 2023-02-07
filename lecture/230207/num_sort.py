T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    for m in range(N):
        for n in range(1, N):
            if num_list[n-1] > num_list[n]:
                num_list[n-1], num_list[n] = num_list[n], num_list[n-1]
    print(f'#{t}', *num_list)

