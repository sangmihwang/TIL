
def f(i, k, p):
    global maxP
    if i == k:          # 모든 직원이 일을 맡으면
        if maxP < p:
            maxP = p
        return
    elif maxP > p:
        return

    else:
        for j in range(k):      # j번 업무를 맡은 사람이 없으면
            if u[j] == 0:
                u[j] = 1
                f(i+1, k, p*arr[i][j]/100)
                u[j] = 0
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxP = 1
    u = [0] * N
    f(0, N, 1)
    print(f'#{t} {maxP*100:.6f}')