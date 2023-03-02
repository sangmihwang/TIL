
## 10816_ 숫자카드2

import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))      # [-10 -10 2 3 3 6 7 10 10 10]
M = int(sys.stdin.readline())
q_card = list(map(int, sys.stdin.readline().split()))    # [10 9 -5 2 3 4 5 -10]
card.sort()                             # 이분탐색을 위해 크기 순 정렬

def bin_s(t):
    left, right = 0, N-1
    global cnt
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == t:
            cnt += 1
            card[mid] = -10000001            # 읽은 건 엄청 작은 수로 바꿔서 앞으로 빼줌
            card.sort()
            left = mid                  # 건너뛰는 것 방지 위해 mid부터 셈
        elif t < card[mid]:
            right = mid - 1
        elif t > card[mid]:
            left = mid + 1
    return cnt

for c in q_card:
    if bin_s(c):
        print(cnt)
    else:
        print(0)

# upper bound(상한선) lower bound(하한선)

# def lowerbound(array, target):
#   start, end = 0, len(array)
#   while start < end:
#     mid = (start+end)//2
#     if target <= array[mid]:
#       end=mid
#     else:
#       start=mid+1
#   return start
#
# def upperbound(array, target):
#   start, end = 0, len(array)
#   while start < end:
#     mid = (start+end)//2
#     if target < array[mid]:
#       end=mid
#     else:
#       start=mid+1
#   return start-1