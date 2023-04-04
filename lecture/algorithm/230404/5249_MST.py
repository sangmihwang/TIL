
## SWEA 5249 최소신장트리

def find_set(x):            # 대표 원소를 리턴해주는 함수
    while x != rep[x]:      # 자기 자신이 대표원소가 아니면
        x = rep[x]          # 대표 원소를 리턴해주고
    return x                # 자기가 대표면 자기 리턴

def union(x, y):                # y의 대표원소가 x의 대표원소를 가리키도록
    rep[find_set(y)] = find_set(x)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = []
    rep = [i for i in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append([n1, n2, w])

    # 가중치 기준 오름차순 정렬
    graph.sort(key=lambda x: x[2])

    # N개 정점(V+1), N-1개의 간선 선택
    N = V + 1
    s = 0           # MST 에 포함된 간선의 가중치 합
    cnt = 0
    MST = []

    for u, v, w in graph:
        if find_set(u) != find_set(v):      # 사이클이 생기지 않으면
            cnt += 1
            s+= w
            MST.append([u, v, w])
            union (u,v)
            if cnt == N-1:
                break
    print(f'#{t} {s}')
