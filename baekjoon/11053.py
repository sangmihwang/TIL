# 11053_ 가장 긴 증가하는 부분 수열

N = int(input())
A = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = 1
if A[1] < A[2]:
    dp[2] = 2
else:
    dp[2] = 1

for i in range(2, N+1):
    max_dp = 0
    for j in range(2, i+1):
        if max_dp < dp[j]:
            max_dp = dp[j]
    dp[i] = max_dp + 1
print(dp[N])

