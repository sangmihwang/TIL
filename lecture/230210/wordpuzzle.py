# T = int(input())
# for t in range(1, T+1):
#     N,K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 가로
#     cnt = 0
#     for i in range(N):
#         for j in range(N-K+1):
#             if arr[i][j:j+K] == [1] * K:
#                 if j == 0 and arr[i][j+K] != 1:
#                     cnt += 1
#                 if 0 < j < N-K and arr[i][j+K] != 1 and arr[i][j-1] != 1:
#                     cnt += 1
#                 if j == N-K and arr[i][j-1] != 1:
#                     cnt += 1
#
#     # 세로
#     for j in range(N):
#         s = []
#         for i in range(N-K-1):
#             for ti in range(K+2):
#
#     print(f'#{t} {cnt}')

### 한 값씩 세면서 하려 했으나 실패하고 다시 처음부터
# 끝에 0짜리 행렬 추가 하는 방식으로


def puzzle(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for idx in lst:
            if idx == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for t in range(1, T+1):
    N,K = map(int, input().split())
    arr1 = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]

    arr2 = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            arr2[i][j] = arr1[j][i]

    ans12 = puzzle(arr1) + puzzle(arr2)

    print(f'#{t} {ans12}')


