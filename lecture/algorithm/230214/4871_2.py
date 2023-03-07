def f(v, G):
    if v == G:
        return 1
    else:
        visited[v] = 1
        for w in adjL[v]:
            if visited[w] == 0:     # 인접하고 방문안한 w
                if f(w, G):         # 목적지를 찾고 리턴하는 경우
                    return 1

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V + 1)]       # 인접 리스트
    visited = [0] * (V+1)
    for _ in range(E):
        v, w = map(int, input().split())    # v 출발, w 도착
        adjL[v].append(w)
        # adjL[w].append(v)                 # 방향이 없는 경우
    S, G = map(int, input().split())        # S 출발, G 도착
    print(f'#{tc} {f(S, G)}')