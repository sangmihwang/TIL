
for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_r = [[0] * 100 for _ in range(100)]
    max_p = 0
    for lst in arr:
        for i in range(100):
            for a in range(1, 100 + 1 - i):
                if lst[i:i + a] == lst[i:i + a][::-1]:
                    pal_len = len(lst[i:i + a])
                    if pal_len > max_p:
                        max_p = pal_len
    # max_p_r = 0
    # for i in range(100):
    #     for j in range(100):
    #         arr_r[i][j] = arr[j][i]
    #         for lst in arr_r:
    #             for k in range(100):
    #                 for a in range(1, 100 + 1 - i):
    #                     if lst[k:k + a] == lst[k:k + a][::-1]:
    #                         pal_len = len(lst[k:k + a])
    #                         if pal_len > max_p_r:
    #                             max_p_r = pal_len

    # ans = max_p + max_p_r

    print(f'#{t} {max_p}')
