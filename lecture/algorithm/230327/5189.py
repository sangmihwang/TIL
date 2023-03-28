def f(i, k, e):
    global minV
    if i == k:
        sum = 0                         # 여기서 p[0]==1일 때를 if로 줬었는데 시간이 너무 많이걸림
        for n in range(k-1):            # 그래서 p[0]==1로 이미 주고 f를 1부터 탐색함
            sum += e[p[n]][p[n+1]]      # 그랬더니 시간이 반의 반으로 줄었음
        sum += e[p[-1]][1]
        if sum < minV:
            minV = sum
    else:
        for j in range(k):  # 사용하지 않은 숫자를
            if used[j] == 0:    # used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1     # j번 자리 숫자 사용으로 표시
                f(i+1, k, e)
                used[j] = 0     # j번 자리 숫자를 다른 자리에서 쓸 수 있게


T = int(input())
for t in range(1, T+1):
    N = int(input())
    e = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    A = list(range(1, N+1))
    p = [0] * N
    used = [0] * N
    minV = 9999
    p[0] = 1                # p의 첫번째 값은 무조건 1로 정해져 있기 때문에
    used[0] = 1
    f(1, N, e)
    print(f'#{t} {minV}')




