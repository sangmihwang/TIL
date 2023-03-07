T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = -1
    if N == 1:
        ans = 1
    else:
        for x in range(1, N):
            if x ** 3 > N:          # 먼저 끊어줘야 함
                break
            if x ** 3 == N:
                ans = x
                break

    print(f'#{t} {ans}')


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     ans = -1
#     for x in range(1, N//3):
#         if x**3 == N:             # 없는 경우 끝까지 갈 수 있으므로 시간 초과
#             ans = int(x)
#             break
#
#     print(f'#{t} {ans}')
