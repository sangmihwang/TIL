

## SWEA  1486 장훈이의 높은 선반
## 선택/미선택의 문제

def dfs(n, sm):
    global ans
    # 최소값 구할 때 항상 성공하는 가지치기
    if ans <= sm-B:     # 이미 더 작음
        return
    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return
    # 포함
    dfs(n+1, sm+lst[n])
    # 포함 X
    dfs(n+1, sm)



T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000
    dfs(0, 0)
    print(f'#{t} {ans}')