# T = int(input())
# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [i for i in range(1, 13)]
#     for i in range(1<<N):
#         for j in range(N):
#             if i & (1<<j):
#                 for a in [arr[j]]:
#                     print(a)
#     #                 sum += int(a)
#     #             if sum == K:
#     #                 ans = j
#     #
#     # print(f'#{t} {ans}')
#
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    cnt = 0

    for i in range(1 << 12):
        subset = []
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])           # arr[j]는 부분집합의 요소 하나하나
                sum_v += arr[j]
        if len(subset) == N and sum_v == K:
            cnt += 1

    print('#{} {}'.format(t, cnt))

#


# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1 << n):
#     s = 0
#     for j in range(n):
#         if i & (1 << j):
#             s += arr[j]
#             # print(arr[j], end = '/')
#     if
#     print()
