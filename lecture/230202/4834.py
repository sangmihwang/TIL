T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input()))
    cnt = [0] * 10
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    
    max_val = 0
    for i in range(len(cnt)):
        if cnt[i] >= max_val:
            max_val = cnt[i]
            num = i 

    print(f'#{t+1} {num} {max_val}')



