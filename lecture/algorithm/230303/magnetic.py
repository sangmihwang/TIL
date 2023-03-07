for t in range(1, 11):
    N = int(input())            # 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    # 1은 아래로 2는 위로
    for j in range(100):
        mag = []
        for i in range(100):
            if arr[i][j] != 0:
                mag.append(arr[i][j])       # 맨앞이 2로 시작하거나/ 맨뒤가 1로 시작하면 out
        for m in range(len(mag)-1):                   # 1->2 순서 인 곳이 교착 상태
            if mag[m] == 1 and mag[m+1] == 2:
                cnt += 1

    print(f'#{t} {cnt}')

