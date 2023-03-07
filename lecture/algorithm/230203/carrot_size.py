T = int(input())
for t in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    max_cnt = 1
    for i in range(1, N):
        if C[i] == C[i-1] + 1:
            cnt += 1

        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:                
        max_cnt = cnt
    print(f'#{t+1} {max_cnt}')
