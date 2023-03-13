
## 2805_ 나무 자르기

N, M = map(int, input().split())        # N: 나무의 수 / M: 가져가려는 나무의 길이
tree = list(map(int, input().split()))
start, end = 0, max(tree)


while start <= end:
    mid = (start + end) // 2
    get_tr = 0
    for t in tree:
        if t - mid > 0:
            get_tr += (t - mid)
    if get_tr == M:
        break
    elif get_tr > M:
        start = mid + 1
    elif get_tr < M:
        end = mid - 1


print(mid)