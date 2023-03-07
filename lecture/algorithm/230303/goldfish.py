T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())      # N명 사람/ M초마다 K개의 붕어빵 생성
    time = list(map(int, input().split()))
    time.sort()
    g_fish = [0] * 11113

    for i in range(M, 11112, M):            # 인덱스를 시간(초)으로 붕어빵 개수
        g_fish[i] = K

    for i in range(N):
        if sum(g_fish[:time[i]+1])>= i+1:     # 여태껏 만든 붕어빵 합 > 사람 수
            ans = 'Possible'
        else:
            ans = 'Impossible'
            break
    print(f'#{t} {ans}')