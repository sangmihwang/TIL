
## 1654_ 랜선 자르기

import sys

K, N = map(int, input().split())    # K 영식이 이미 가진 랜선 개수/ N 필요한 랜선 수
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)
ans = []

while start <= end:
    mid = (start + end)//2
    cnt = 0
    for l in lan:
        cnt += (l // mid)
    if cnt < N:         # 개수가 적으면 길이를 줄여야 
        end = mid-1
    elif cnt >= N:
        start = mid +1

print(end)


# 반례
# 5 11
# 60 30 20 15 12



