# 2579_ 계단 오르기

N = int(input())
s = [0] + [int(input()) for _ in range(N)]      # 계단 점수 인덱스 맞춤
dp = [0] * (N+1)                                # 각 계단 최대 점수 [dp]
dp[0] = 0                                       # 시작 0점부터
dp[1] = s[1]                                    # 첫번째 계단은 무조건 첫번째 점수
if N == 1:
    dp[1] = s[1]
elif N > 1:
    dp[2] = s[1]+s[2]
    for i in range(3, N+1):               # i-1 밟은 경우 i-2 밟음 안 됨, i-2 밟은 경우
        dp[i] = max(dp[i-3] + s[i-1], dp[i-2]) + s[i]
print(dp[N])



## dp[1]일 때를 간과했음. 무조건 dp[1]은 s[1]이므로 지정해주고 그 다음 시작해야함