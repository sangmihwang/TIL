
## 11725_ 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)


def DFS(n):
    for i in Tree[n]:
        if parent[i] == 0:
            parent[i] = n
            DFS(i)

N = int(sys.stdin.readline())
Tree = [[] for _ in range(N+1)]
parent = [0] * (N + 1)              # 인덱스 맞추기 위해 +1
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split()) 
    Tree[a].append(b)             # 부모 자식 상관없이 연결된 상황
    Tree[b].append(a)
# print(Tree)          #[[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
            
DFS(1)
for i in range(2, N+1):
    print(parent[i])





# 딕셔너리
# 좌우자식 리스트도 해봤는데 이진 아니어서 취소
