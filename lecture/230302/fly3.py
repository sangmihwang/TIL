T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())            # N*N 배열    # M: 스프레이 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N):                          # 십자 모양
        for j in range(N):
            kill = 0                            # 새로운 시작점에서 kill 값 초기화
            kill += arr[i][j]                   # 시작점 파리수
            for l in range(1, M):
                if i-l >= 0:                    # 배열 range 벗어날 것 방지
                    kill += arr[i-l][j]         # 상
                if j-l >= 0:
                    kill += arr[i][j-l]         # 좌
                if j+l <= N-1:
                    kill += arr[i][j+l]         # 우
                if i+l <= N-1:
                    kill += arr[i+l][j]         # 하

            if kill > max_kill:
                max_kill = kill

    for i in range(N):                          # 대각선 모양
        for j in range(N):
            kill = 0                            # 새로운 시작점에서 kill 값 초기화
            kill += arr[i][j]                   # 시작점 파리수
            for l in range(1, M):
                if i-l >= 0 and j-l >= 0:       # 배열 range 벗어날 것 방지
                    kill += arr[i-l][j-l]       # 왼쪽 위
                if j-l >= 0 and i+l <= N-1:
                    kill += arr[i+l][j-l]       # 왼쪽 아래
                if i-l >= 0 and j+l <= N-1:
                    kill += arr[i-l][j+l]         # 오른쪽 위
                if i+l <= N-1 and j+l <= N-1:
                    kill += arr[i+l][j+l]         # 오른쪽 아래

            if kill > max_kill:
                max_kill = kill

    print(f'#{t} {max_kill}')


