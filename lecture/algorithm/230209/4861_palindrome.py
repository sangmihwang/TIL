T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):                    # 가로
        for j in range(N-M+1):
            s = arr[i][j:j+M]

            str = ''.join(s)
            if str == str[::-1]:
                ans = str
    s = []
    for j in range(N):                   # 세로
        for w in range(N-M+1):
            for i in range(M):           # 세로에서 처음부터 끝까지 리스트 다 구해서 오답
                a = arr[w+i][j]          # 주어진 M개만큼만 리스트 구해야
                s.append(a)

            str = ''.join(s)
            if str == str[::-1]:
                ans = str
            s = []

    print(f'#{t} {ans}')

