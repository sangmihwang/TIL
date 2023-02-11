T = int(input())
for t in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                pass
            else:
                if A[i] == A[j]:
                    ans = 'NO'
                    break
                else:
                    ans = 'YES'
    print(f'#{t} {ans}')