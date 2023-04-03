
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs1(v, k):      # 중복없이 빠짐없이
    visited[v] = 1      # 중복방지용
    print(v)
    for w in range(1, k+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs1(w, k)

def dfs2(s, k):
    stack = []
    visited = [0]*(k+1)
    v = s
    while True:
        if visited[v] == 0:
            print(v)


            for w in range(1, k+1):
                if adjM[v][w] and visited[w] == 0:
                    stack.append(v)
                    v = w
                    break
        else:
            if stack:
                v = stack.pop()
            else:       # 스택이 비어있으면 / 더이상 가야할 곳이 없으면
                break

def dfs3(v, k, g):
    global cnt
    if v== g:
        cnt+= 1
    else:
        visited[v] = 1
        for w in range(1, k+1):
            if adjM[v][w] == 1 and visited[w] == 0:
                dfs3(w, k, g)
        visited[v] = 0

def dfs4(v, k):
    sp = -1
    stack = [0] * k
    visited = [0] * (k+1)       # 스택 생성, 스택포인터 초기화
    # 시작점 push (stack을 탐색할 정점 목록으로 활용/ 가지않고 남겨놓은 정점)
    sp += 1         # push와 방문표시 (목록에 이미 올라가있음)
    stack[sp] = v
    visited[v] = 1
    while sp > -1:    # 스택이 비어있지 않으면    # while stack:    # stack.append(), stack.pop()인 경우
        v = stack[sp]       # pop()
        sp -= 1
        print(v)
        for w in range(1, k):
            if adjM[v][w] and visited[w] == 0:
                sp += 1              # push와 방문표시 (목록에 올림)
                stack[sp] = v
                visited[w] = 1

    return


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
visited = [0] *(V+1)

# dfs(1, V)
# dfs2(1, V)
# dfs3(1, V, 7)
dfs4(1, V)
print()
print(cnt)


