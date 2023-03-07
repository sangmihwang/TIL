T = int(input())
for t in range(T):
    N = int(input())
    ser = str(input())
    lis = list(ser)
    cnt = 0
    max_cnt = 0
    for i in range(N):
        if lis[i] == '1':
            cnt += 1                # 마지막 숫자가 1인 경우 
                                    # 그걸 max에 미처 받아오지 못하고 
                                    # 그대로 1 부족하게 출력           
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0
    if max_cnt < cnt:                # 그래서 여기서 최종적으로
        max_cnt = cnt                # 한 번 더 max_cnt 와 cnt 비교
    print(f'#{t+1} {max_cnt}')
        

