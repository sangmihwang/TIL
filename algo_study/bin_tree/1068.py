def dfs(v):
    lst[v] = -2     # 지워지는 노드의 부모노드를 -2로 바꾸기
    for i in range(N):
        if v == lst[i]:   # 지우고자 하는 노드 v가 lst[i]에 들어있으면 lst[i]는 v의 자식
            dfs(i)  # i의 자식도 지움


N = int(input())
lst = list(map(int, input().split()))
erase = int(input())

dfs(erase)
cnt = 0

for i in range(N):
    if lst[i] != -2 and i not in lst:   # 값이 -2 가 아니고 해당 노드를 부모로 하는 노드가 부모 배열에 없을 경우-> 리프노드
        cnt += 1
print(cnt)