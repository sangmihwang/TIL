# 11053_ 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:   # 마지막 수가 제일 크고 dp가 작은 상태면
            dp[i] = dp[j]                   # 마지막 수 dp를 그걸로 갱신
    dp[i] += 1                  # 해당 수 dp 값 (+1)

print(max(dp))

