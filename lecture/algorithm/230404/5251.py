
## 5251 SWEA 최소 이동 거리

def dijkstra(s, V):     # 출발 번호 s, 도착 정점 번호 V
    U = [0] * (V+1)     # 최소 비용이 결정됐는지 안됐는지 확인 리스트
    U[s] = 1            # 출발하니까 지난 걸로
    for i in range(V+1):        # s에서 정점 i로가는 비용
        D[i] = adjM[s][i]       # 일단 s에서 가는 모든 경우의 비용 D에 추가

    # 정점 N개
    for _ in range(N-1):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]: # 길이 확정되지않았고 최소보다 작으면
                w = i
                minV = D[i]
        U[w] = 1            # 길 확정시킴
        for v in range(V+1):
            if 0 < adjM[w][v] < INF:        # w에 인접인 v의 조건
                D[v] = min(D[v], D[w] + adjM[w][v])


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())    # 마지막 번호 N, 도로 개수 E
    INF = 10000
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    D = [0] * (N + 1)
    dijkstra(0, N)
    print(f'#{t} {D[-1]}')