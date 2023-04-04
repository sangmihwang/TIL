
## SWEA 등산로 조성




T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())    # N 지도 한 변의 길이, K 공사 가능 깊이
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대높이 찾기
    maxH = 0
    for i in range(N):
        for j in range(N):
            if maxH < arr[i][j]:
                maxH = arr[i][j]
    for i in range(N):
        for j in range(N):
            if maxH < arr[i][j]:
    print(f'#{t} {}')