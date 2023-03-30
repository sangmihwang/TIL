
## 5207 SWEA 이진탐색

def bin_s(A, l, r, tg):    # 찾으려는 수
    if l <= r:
        m = (l+r)//2
        if tg == A[m]:
            lst.append(2)
            return
        if tg < A[m]:
            lst.append(-1)               # 왼쪽으로 갔다는 거 표시
            bin_s(A, l, m-1, tg)
        elif tg > A[m]:
            lst.append(1)              # 오른쪽으로 갔다는 거 표시
            bin_s(A, m+1, r, tg)
        else:
            return                       # 타겟이 없으면 끝

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0

    for tg in B:
        lst = []
        bin_s(A, 0, len(A)-1, tg)

        i = 0                           # 양쪽 번갈아갔는지 확인
        while i < len(lst)-1:
            if lst[i] == lst[i+1]:        # 같은쪽 갔으면
                break
            else:
                i += 1
        if i == len(lst)-1 and 2 in lst:
            cnt += 1

    print(f'#{t} {cnt}')


# def bin_s(arr, l, r, tg):         # 찾으려는 수
#     if r == 0:                    # 리스트에 원소 하나면
#         if tg == arr[0]:          # 타겟이면 바로 찾은거니까
#             lst.append(2)
#             return
#     else:
#         m = (l + r) // 2
#         if tg == arr[m]:
#             lst.append(2)
#             return
#         left = arr[l:m]
#         right = arr[m + 1:]
#
#         if left == [tg] or right == [tg]:
#             lst.append(2)
#             return
#         else:
#             if left:
#                 if tg <= left[-1]:
#                     lst.append(-1)        # 왼쪽으로 갔다는 거 표시
#                     bin_s(left, 0, len(left) - 1, tg)
#             if right:
#                 if tg >= right[0]:
#                     lst.append(1)         # 오른쪽으로 갔다는 거 표시
#                     bin_s(right, 0, len(right) - 1, tg)
#             else:
#                 return            # 타겟이 없으면 끝
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     A.sort()
#     B.sort()
#     cnt = 0
#
#     for tg in B:
#         lst = []
#         bin_s(A, 0, len(A) - 1, tg)
#
#         i = 0                 # 양쪽 번갈아갔는지 확인
#         while i < len(lst) - 1:
#             if lst[i] == lst[i + 1]:          # 같은쪽 갔으면
#                 break
#             else:
#                 i += 1
#         if i == len(lst) - 1 and 2 in lst:
#             cnt += 1
#
#     print(f'#{t} {cnt}')