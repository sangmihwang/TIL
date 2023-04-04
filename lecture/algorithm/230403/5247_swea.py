
## SWEA 5247 연산


## 재귀 말고 BFS 로 해야함

# def f(n, m, k):
#     if n == m:
#         return k
#
#     if n-1 > 0 and visited[n-1] == 0:
#         f(n-1,M, k+1)
#         visited[n-1] = 1
#     if 1000000 >= n+1  and visited[n+1] == 0:
#         f(n+1,M, k+1)
#         visited[n+1] = 1
#     if 1000000 >= n*2  and visited[n*2] == 0:
#         f(n*2,M, k+1)
#         visited[n*2] = 1
#     if n-10 > 0 and visited[n-10] == 0:
#         f(n-10,M, k+1)
#         visited[n-10] = 1


# def f(n, e):     # n 현재 위치, e 종점
#     visited[n] = 1
#     stack = [n]
#
#     if n == e:
#         return
#     else:
#         while stack:
#             tmp = stack.pop(0)
#             for i in [tmp+1, tmp-1, tmp*2, tmp-10]:
#                 if 0 < i <1000000 and visited[i] == 0:
#                     stack.append(i)
#                     visited[i] = visited[tmp] + 1

from collections import deque

def f(s, e):
    while q:
        tmp = q.popleft()
        if tmp == e:
            return
        for i in [tmp + 1, tmp - 1, tmp * 2, tmp - 10]:
            if 0 < i <= 1000000 and visited[i] == 0:
               q.append(i)
               visited[i] = visited[tmp] + 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0]*1000001
    visited[N] = 1
    q= deque([N])
    f(N, M)

    print(f'#{t} {visited[M]-1}')


def f(s, e):
    while stack:
        tmp = stack.pop(0)
        if tmp == e:
            return
        for i in [tmp + 1, tmp - 1, tmp * 2, tmp - 10]:
            if 0 < i <= 1000000 and visited[i] == 0:
                stack.append(i)
                visited[i] = visited[tmp] + 1


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    visited[N] = 1
    stack = [N]
    f(N, M)

    print(f'#{t} {visited[M] - 1}')