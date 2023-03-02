
## 10816_ 숫자카드2

N = int(input())
card = list(map(int, input().split()))      # [-10 -10 2 3 3 6 7 10 10 10]
M = int(input())
q_card = list(map(int, input().split()))    # [10 9 -5 2 3 4 5 -10]
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
            left = mid + 1
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
