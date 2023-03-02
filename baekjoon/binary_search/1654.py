
## 1654_ 랜선 자르기

import sys

K, N = map(int, input().split())    # K 영식이 이미 가진 랜선 개수/ N 필요한 랜선 수
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lan:
        cnt += (l // mid)
    if cnt == N:
        ans = mid
        break
    elif cnt < N:           # 목표값보다 라인 수가 작으면 기준 길이를 줄임
        end = mid - 1
    elif cnt > N:
        start = mid + 1     # 목표값보다 라인 수가 크면 기준 길이를 늘림

print(ans)





