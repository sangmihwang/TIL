
# dfs 부분수열의 합
def dfs(n, sum):        # (숫자 순서, 합)
    global cnt
    if n == N:          # 마지막 수 지났으면
        if sum == K:        # 합 K 되면 멈춰줘야 중복 안됨 ##### 땡 ######
            cnt += 1        # 멈춰주는게 아니고 인덱스 끝까지는 일단 훌터야함 선택/미선택이기 때문
        return
    dfs(n+1, sum + A[n])        # n번째 수 선택함
    dfs(n+1, sum)               # n번째 수 선택 안 함


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)

    print(f'#{t} {cnt}')