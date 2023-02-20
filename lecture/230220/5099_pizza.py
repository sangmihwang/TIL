T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))     # 치즈 양
    oven = []
    for i in range(N):
        oven.append(i)          # 피자번호
    last = N-1                  # 화덕에 들어간 마지막 피자번호 (화구 수 - 1)

    while oven:                 # 더이상 피자가 없을 때까지 회전
        num = oven.pop(0)       # 입구로 돌아온 피자 번호 (맨 앞 제거)
        pizza[num] //= 2        # 한바퀴 돌면서 절반이 녹음
        if pizza[num] > 0:      # 완전히 녹지 않은 경우
            oven.append(num)    # 계속 오븐에 둠(맨 뒤로)
        else:                   # 치즈 다 녹았으면 (pizza[num] == 0)
            ans = num           # 마지막 피자
            if last + 1 < M:    # 아직 화덕에 들어가지 않은 피자가 있으면
                last += 1       # 추가로 화덕에 투입
                oven.append(last)

    print(f'#{t} {ans+1}')
