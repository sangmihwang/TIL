T = int(input())
di = [0, -1, 0, 1]      # 좌 상 우 하
dj = [-1, 0, 1, 0]
for t in range(1, T+1):
    N = int(input())
    num = [0] * (N*N+2)     # 인덱스 맞추려고 앞에 한 칸 더
    cnt = 1
    max_cnt = 0                  # 인덱스 맞추려고 앞에 상하좌우 0 더 씀
    arr = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0]
                          for _ in range(N)] + [[0] * (N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(4):
                if arr[i+di[k]][j+dj[k]] == arr[i][j] + 1:
                    num[arr[i][j]] = 1        # 연속된 수면 num[] 1로

    # n 옆에 연속된 수 있으면 num[n] = 1
    # 연속된 개수 알려면 연속된 1 개수 구하면 됨
    # 인덱스는 그 중 제일 작은 거

    for n in range(len(num)-2, -1, -1):        # 제일 작은 인덱스니까 뒤에서부터 갱신
                                                # 인덱스 0도 포함해야돼서 -1까지로 해야함
        if num[n] == 1:                       # 연속된 수면
            cnt += 1                          # 카운트 +1
        else:                                   # 연달아 1 아니면
            if max_cnt <= cnt:
                max_cnt = cnt                   # 최대 카운트 지정
                ans = n + 1
            cnt = 1                             # cnt 초기화

    print(f'#{t} {ans} {max_cnt}')




