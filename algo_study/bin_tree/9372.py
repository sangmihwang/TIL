
## 9372_ 상근이의 여행

import sys

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
            print(check)
    return cnt

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]            # 인덱스 맞춰주기 위해 +1
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())   # a와 b 연결
        graph[a].append(b)
        graph[b].append(a)
    check = [0] * (N+1)

    print(dfs(1, 0))
