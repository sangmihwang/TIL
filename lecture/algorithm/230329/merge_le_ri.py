#
# ## SWEA 5204 병합 정렬
#
# def merge(left, right):
#     global cnt
#     if left[-1] > right[-1]:
#         cnt += 1
#     i = j = k = 0           # 함수가 호출될때마다 새로운 left, right로
#                             # 시작하기 때문에 0으로 리셋
#     while i < len(left) or j < len(right):
#         while i < len(left) and j < len(right):
#             # 왼쪽 1번과 오른쪽 1번 비교
#             # 왼쪽 꺼가 작으면
#             if left[i] <= right[j]:
#                 tmp[k] = arr[i]
#                 i += 1
#             elif left[i] > right[j]:
#                 tmp[k] = arr[j]
#                 j += 1
#             k += 1
#
#         # right는 다 들어가고 left 원소만 남음
#         while i < len(left):
#             tmp[k] = left[i]
#             i += 1
#             k += 1
#         # left는 다 들어가고 right 원소만 남음
#         while j < len(right):
#             tmp[k] = right[j]
#             j += 1
#             k += 1
#     return tmp
#
# def msort(m):
#     if len(m) == 1:
#         return m
#     middle = len(m)//2
#     left = m[:middle]
#     right = m[middle:]
#
#     left = msort(left)
#     right = msort(right)
#     return merge(left, right)
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     tmp = [0] * (N+2)
#     cnt = 0
#     msort(arr)
#
#     print(f'#{t} {tmp[N//2]} {cnt}')
#
#
#
def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    tmp = [0]*(len(left)+len(right))
    i = j = k = 0           # 함수가 호출될때마다 새로운 left, right로
                            # 시작하기 때문에 0으로 리셋

    while i < len(left) and j < len(right):
        # 왼쪽 1번과 오른쪽 1번 비교
        # 왼쪽 꺼가 작으면
        if left[i] <= right[j]:
            tmp[k] = left[i]        # 원본에 arr로 되어있네요
            i += 1
        else:
            tmp[k] = right[j]
            j += 1
        k += 1

    # right는 다 들어가고 left 원소만 남음
    while i < len(left):
        tmp[k] = left[i]
        i += 1
        k += 1
    # left는 다 들어가고 right 원소만 남음
    while j < len(right):
        tmp[k] = right[j]
        j += 1
        k += 1
    return tmp

def msort(m):
    if len(m) == 1:
        return m
    middle = len(m)//2
    left = m[:middle]
    right = m[middle:]

    left = msort(left)
    right = msort(right)
    return merge(left, right)



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = msort(arr)

    print(f'#{t} {arr[N//2]} {cnt}')