
## 18352_ 특정거리의 도시 찾기

# from collections import deque

# N, M, dist, start = map(int, input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]   # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# for _ in range(M):          # [[0], [0, 2, 3], [0, 3, 4], [0], [0]]
#     a, b = map(int, input().split())
#     # doro[a].append(b)
#     arr[a][b] += 1

# doro = [0 for _ in range(N+1)]      # [[0], [0], [0], [0], [0]]

# q = deque[(start)]
# tmp = q.popleft()

# for i in range(1, N+1):
    


# print(doro)
# print(arr)



from collections import deque
import sys
input = sys.stdin.readline

N, M, dist, start = map(int, input().split())
doro = [[] for _ in range(N+1)]      # [[], [], [], [], []]
distance = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    doro[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in doro[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == dist:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(start)
