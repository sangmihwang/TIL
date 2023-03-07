# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())    # N: 보드 크기 M: 돌 놓는 횟수
#     board = [[0]*N for _ in range(N)]
#
# didj = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
# op = [0, 2, 1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     brd = [[0] * (N + 2) for _ in range(N + 2)]
#     stone = [list(map(int, input().split())) for _ in range(M)]
#     B, W = 1, 2
#
#     brd[N // 2][N // 2] = W
#     brd[N // 2][N // 2 + 1] = B
#     brd[N // 2 + 1][N // 2] = B
#     brd[N // 2 + 1][N // 2 + 1] = W
#
#     for j, i, bw in stone:
#         brd[i][j] = bw
#         for di, dj in didj:
#             flip = []
#             ni, nj = i + di, j + dj
#             while brd[ni][nj] == op[bw]:
#                 flip.append((ni, nj))
#                 ni += di
#                 nj += dj
#             if brd[ni][nj] == bw:  # 같은 색을 만나면 모두 뒤집기
#                 for ni, nj in flip:
#                     brd[ni][nj] = bw
#     cnt = [0] * 3
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             cnt[brd[i][j]] += 1


























