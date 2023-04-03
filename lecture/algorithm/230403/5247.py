'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, k):      # s 탐색시작 생성번호, k 마지막 정점번호
    q =[]
    visited = [0]*(k+1)
    q.append(s)
    visited[s] = 1
    while q:        # 큐가 비어있지 않으면 반복
        v = q.pop(0)    # v <- 디큐
        print(v)        # v 방문(처리)  # if v ==goal: break 하던가
        for w in range(1, k+1):
            if adjM[v][w] ==1 and visited[w] == 0:
                q.append(w)         # 인큐
                visited[w] = 1 + visited[v]      # 방문 표시



V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬
adjL = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1
    adjL[n1].append(n2)
    adjL[n2].append(n1)