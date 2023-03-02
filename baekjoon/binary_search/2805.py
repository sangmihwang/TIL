
## 2805_ 나무 자르기

N, M = map(int, input().split())        # N: 나무의 수 / M: 가져가려는 나무의 길이
tree = list(map(int, input().split()))
start, end = 1, max(tree)
ans = 0

while start <= end:


