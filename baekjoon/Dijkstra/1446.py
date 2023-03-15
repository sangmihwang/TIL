
## 1446 _ 지름길


import sys
input = sys.stdin.readline

N, D = map(int, input().split())
road = []
dist = [i for i in range(D+1)]

for _ in range(N):
    a, b, d = map(int, input().split())
    road.append([a, b, d])

for i in range(D+1):
    if i > 0:
        dist[i] = min(dist[i], dist[i-1]+1)
    for a, b, d in road:
        if i == a and b <= D and dist[i]+d < dist[b]:
            dist[b] = dist[i]+d
print(dist[D])