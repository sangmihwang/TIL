T = int(input())
for t in range(1, T+1):
    arr_ans = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for c in range(N):
        if arr[c][-1] == 1:
            for i in range(arr[c][0], arr[c][2]+1):
                for j in range(arr[c][1], arr[c][3]+1):
                    # if arr_ans[i][j] == 0 or arr_ans[i][j] == 2:
                        arr_ans[i][j] += 1
        else:
            for i in range(arr[c][0], arr[c][2]+1):
                for j in range(arr[c][1], arr[c][3]+1):
                    # if arr_ans[i][j] == 0 or arr_ans[i][j] == 1:
                        arr_ans[i][j] += 2               
    # print(arr_ans)
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr_ans[i][j] ==3:
                cnt += 1 
    print(f'#{t} {cnt}')
    



