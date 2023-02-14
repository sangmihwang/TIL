
## 재귀

def f(i, k):
    if i == k:      # 목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

# A = [i for i in range(1000)]        # 맥시멈 깊이 넘어섬
A = [10, 20, 30]
B = [0] * 3
f(0, 3)

## DFS(깊이우선탐색)
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0] * (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print()