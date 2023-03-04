# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     color = [list(input()) for _ in range(N)]
#     for a in range(1, N - 1):
#         arr = [[0] * M for _ in range(N)]
#         for i in range(N):
#             for j in range(M):
#                 arr[i][j] = color[i][j]
#     min_cnt = 2500
#     for a in range(1, N - 2):       # 첫번째 경계
#         for b in range(a + 1, N - 1):   # 두번째 경계
#             cnt = 0
#             for i in range(a):          # 0부터 a-1까지
#                 for j in range(M):
#                     if arr[i][j] != 'W':
#                         arr[i][j] = 'W'
#                         cnt += 1
#             for i in range(a, b):     # a부터 b-1까지
#                 for j in range(M):
#                     if arr[i][j] != 'B':
#                         arr[i][j] = 'B'
#                         cnt += 1
#             for i in range(b, N):
#                 for j in range(M):
#                     if arr[i][j] != 'R':
#                         arr[i][j] = 'R'
#                         cnt += 1
#             if cnt < min_cnt:
#                 min_cnt = cnt
#     print(f'#{t} {min_cnt}')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    color = [list(input()) for _ in range(N)]

    min_cnt = 2500
    for a in range(N - 2):       # 첫번째 경계
        for b in range(a + 1, N - 1):   # 두번째 경계
            cnt = 0
            for i in range(a+1):          # 0부터 a까지
                for j in range(M):
                    if color[i][j] != 'W':
                        cnt += 1
            for i in range(a+1, b+1):     # a+1부터 b까지
                for j in range(M):
                    if color[i][j] != 'B':
                        cnt += 1
            for i in range(b+1, N):
                for j in range(M):
                    if color[i][j] != 'R':
                        cnt += 1
            if min_cnt > cnt:       # 아래 식과 같은 순서면 보기에 편합니다.
                min_cnt = cnt
    print(f'#{t} {min_cnt}')