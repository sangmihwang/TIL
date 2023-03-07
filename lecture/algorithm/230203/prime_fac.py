T = int(input())
num = [2, 3, 5, 7, 11]
for t in range(T):
    N = int(input())
    cnt = [0] * 5
    for j in range(5):
        for i in range(N):
            if N % num[j] == 0:
                N = int(N/num[j])
                cnt[j] += 1
            else:
                break
   
    
    print(f'#{t+1}',*cnt)


