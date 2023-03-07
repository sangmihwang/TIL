def max_palin(arr):
    max_p = 0
    for lst in arr:
        for i in range(100):
            for a in range(1, 100+1-i):
                if lst[i:i+a] == lst[i:i+a][::-1]:
                    pal_len = len(lst[i:i+a])
                    if pal_len > max_p:
                        max_p = pal_len
    return max_p

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_r = [[0]*100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            arr_r[i][j] = arr[j][i]


    ans = max(max_palin(arr), max_palin(arr_r))

    print(f'#{t} {ans}')



