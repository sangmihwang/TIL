
## 1952 SWEA 수영장
## 선택의 경로 : 일/월/분기/년
##  n : 월(번호)index  => n>12 : 종료조건

def dfs(n, sm):
    global ans

    if ans <= sm:
        return              # 가지치기
    if n > 12:
        ans = min(ans, sm)
        return
    dfs(n+1, sm + day*lst[n])       # 일
    dfs(n+1, sm + mon)              # 월
    dfs(n+3, sm + mon3)             # 분기
    dfs(n+12, sm + year)            # 연


T = int(input())
for t in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0]+ list(map(int, input().split()))

    # 백트래킹
    ans = 365 * 3000        # 워스트 테이스 (금액 최대)
    dfs(1, 0)   # 1월부터 시작, 가격 0 시작

    # 규칙성 찾기 (dp)
    s = [0] *13
    for i in range(1, 13):
        # 가능한 방법 중 i달 까지의 최소 비용
        s[i] = s[i-1]*day*lst[i]       # 일
        s[i] = min(s[i], s[i-1]+mon)    # 월
        if i >= 3:
            s[i] = min(s[i], s[i-3]+mon3)   # 분기
        if i >= 12:
            s[i] = min(s[i], s[i-12] + year)    # 연
    ans = s[12]
    print(f'#{t} {ans}')