# def f(i, k):
#     global minV
#     if i == k:      # 순열 완성
#         s =0
#         for j in range(N):
#             s += arr[j][p[j]]
#         if minV > s:
#
#         return
#     else:
#         for j in range(i, N):
#             p[i], p[j] = p[i], p[j]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     p = [i for i in range(N)]       # p[i] i행에서 선택한 열
#     minV = 0
#     f(0, N)


def f(i, k, s):                 # s 앞에서 선택한 원소의 합
    global minV
    global cnt
    cnt += 1
    if i == k:                  # 순열 완성
        if minV > s:
            minV = s
        return
    elif s >= minV:
        return
    else:
        for j in range(i, N):   # p[i]의 숫자를 자신부터 오른쪽과 교환해봄
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]           # p[i] i행에서 선택한 열
    minV = 100                          # 10이하 자연수 10개 이하
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {minV}')












def sol():













T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]