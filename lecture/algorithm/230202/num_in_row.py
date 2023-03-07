T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    for j in range(N):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i] :
                arr[i], arr[i+1] = arr[i+1], arr[i]  
 
    print(f'#{t+1}',*arr)
                