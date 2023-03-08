
## 1260 _ DFS와 BFS

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split()) # 정점 수, 간선 수, 시작정점
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [0] * (N+1)
stack = [V]
ans = []
flag = True
while flag:
    n = stack.pop(0)
    visited[n] = 1
    ans.append(n)
    for i in range(len(lst[n])):
        if visited[lst[n][i]] == 0:
            stack.append(lst[n][i])
            break
            
            
            
print(*ans)
        

     

