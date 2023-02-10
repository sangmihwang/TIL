for t in range(1, 11):
    L = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0

    # 가로
    for i in range(8):
        for j in range(9-L):
            a = arr[i][j:j+L]
            if a == a[::-1]:
                cnt += 1

    # 세로
    s = []
    for j in range(8):
        for i in range(9-L):
            for ti in range(L):
                b = arr[i+ti][j]
                s.append(b)
            if s == s[::-1]:
                cnt += 1
            s = []
    print(f'#{t} {cnt}')




