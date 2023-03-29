def merge(left, right):
    pass

def msort(m):
    global cnt
    if len(m) == 1:
        return m
    middle = len(m)//2
    left = m[0:middle]
    right = m[middle:]
    if left[-1] > right[-1]:
        cnt += 1
    left = msort(left)
    right = msort(right)
    return merge(left, right)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    msort(0, N-1)