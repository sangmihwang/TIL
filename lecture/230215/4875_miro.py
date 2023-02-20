T = int(input())
di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                Si, Sj = i, j           # 시작점
    stack = []                          # 현재 위치
    stack.append((Si, Sj))
    flag = False
    while stack:
        Si, Sj = stack.pop()
        for d in di:
            i, j = Si+d[0], Sj+d[1]
            if 0 <= i < N and 0 <= j < N:
                if miro[i][j] == 0:
                    stack.append((i, j))
                    miro[i][j] = 1
                    continue
                if miro[i][j] == 3:
                    flag = not flag
                    break
        if flag:                            # while문 탈출 위해
            break
    if flag:
        ans = 1
    else:
        ans = 0
    print(f'#{t} {ans}')

# a = [1] + [2]             # 리스트 하나로 합쳐짐
# print(a)          # [1,2]

