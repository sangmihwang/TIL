
# 격자판의 숫자 이어붙이기

def dfs(n, num, x, y):
    if n == 7:
        ans.add(num)
        return
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    for (dx, dy) in d:
        if 0 <= x+dx <= 3 and 0 <= y+dy <= 3:
            dfs(n+1, num*10 + arr[x+dx][y+dy], x+dx, y+dy)



T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    cnt = 0
    for i in range(4):
        for j in range(4):
            dfs(0, 0, i, j)        # 숫자 개수, 생성 숫자 배열

    print(f'#{t} {len(ans)}')