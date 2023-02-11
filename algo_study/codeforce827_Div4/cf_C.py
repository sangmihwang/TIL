T = int(input())
for t in range(1, T+1):
    arr = [list(input()) for _ in range(8)]
    arr_r = [[0]*8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            arr_r[i][j] = arr[j][i]

    for i in range(8):
            if arr[i][:] == ['R'] * 8:
                ans = 'R'
            if arr[i][:] == ['B'] * 8:
                ans = 'B'
            if arr_r[i][:] == ['R'] * 8:
                ans = 'R'
            if arr_r[i][:] == ['B'] * 8:
                ans = 'B'

    print(f'#{t} {ans}')