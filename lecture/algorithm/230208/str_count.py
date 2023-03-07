T = int(input())
for t in range(1, T+1):
    str1 = list(n for n in input())
    str2 = list(n for n in input())
    max_cnt = 0
    for a in str1:
        cnt = 0
        for b in str2:
            if a == b:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{t} {max_cnt}')


