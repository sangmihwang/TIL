for t in range(1, 11):
    T = int(input())
    arr = [[0] + list(map(int, input().split()))+[0] for _ in range(100)]
    # for lst in arr:
    #     lst.insert(0,0)
    #     lst.append(0)

    i = 0
    j = 0
    cnt = 0
    arr_c = arr.copy()                  # 깊은복사
    while i < 100 and j < 101:          # 반복이 안 됨 지금
            if arr_c[i][j] == 1:          # 첫째줄 1인 곳에서 시작
                arr_c[i][j] = 0           # 지나온 길은 0으로 # 복사본 만드는게 낫다
                if arr_c[i][j+1] == 1:        # 오른쪽이 1이면 오른쪽으로
                    j += 1
                if arr[i][j-1] == 1:        # 왼쪽이 1이면 왼쪽으로
                    j -= 1
                else:                       # 둘 다 아니면 아래로
                    i += 1
                cnt += 1
            else:
                j += 1


    print(f'#{t} {cnt}')

