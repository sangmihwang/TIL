
## 5248 SWEA 그룹 나누기

def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)      # y의 대표원소를 x의 대표원소로 바꿔줌

def count(l):
    cnt = 0
    for i in range(1, len(l)):
        if i == l[i]:
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    rep = [i for i in range(N+1)]

    for i in range(M):
        union(min(lst[i*2], lst[i*2+1]), (max(lst[i*2], lst[i*2+1])))   # 큰 수의 대표원소를 작은 수의 대표원소로

    print(rep)
    print(f'#{t} {count(rep)}')



