
def prim(V):
    INF = 100

    key = [INF] * (V+1)     # 각 정점을 MST에 연결하는데 필요한 비용
    key[0] = 0           # 0번 정점부터
    MST = [0]
    for _ in range(V):      # 나머지 V개의 정점에 대해
        # MST에 포함되지 않은 정점 중 key가 최소인 u 찾기
        u = 0
        minV = INF
        for i in range(V+1):
            if i not in MST and minV >key[i]:
                u = i
                minV = key[i]
        MST.append(u)
        # u에 인접인 v에 대해 비용 갱신 시도
        for v in range(V+1):
            if v not in MST and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])

    return sum(key)



V, E = map(int, input().split())
adjM = [[0] *(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w      # 방향이 없으므로 추가 필수


    print(prim(V))