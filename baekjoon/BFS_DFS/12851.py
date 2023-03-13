
## 12851_ 숨바꼭질2


import sys
input = sys.stdin.readline
from collections import deque


def BFS(N, K):
    q = deque([N])
    visited[N] = 1
    if N == K:
        return 0
    else:
        while q:
            tmp = q.popleft()
            for i in [tmp-1, tmp+1, 2*tmp]:
                if 0 <= i <= 100000 and visited[i] == 0:
                    if i == K:
                        return visited[tmp]
                    else:
                        q.append(i)
                        visited[i] = visited[tmp] + 1



def BFS2(N, K):
    cnt = 0
    q = deque([N])
    visited[N] = 1
    if N == K:
        return 1
    else:
        while q:
            tmp = q.popleft()
            for i in [tmp-1, tmp+1, 2*tmp]:
                if cnt == 0:
                    if 0 <= i <= 100000 and visited[i] == 0:
                        if i == K:
                            cnt += 1
                        else:
                            q.append(i)
                            visited[i] = visited[tmp] + 1
                else:
                    if 0 <= i <= 100000:
                        if i == K:
                            cnt += 1
                        else:
                            q.append(i)
                            visited[i] = visited[tmp] + 1

    return cnt

N, K = map(int, input().split())
visited = [0]*100001

print(BFS(N, K), BFS2(N, K))







N, K = map(int, input().split())
visited = [0]*100001
print(BFS(N, K))




