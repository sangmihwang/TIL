
## SWEA 5208 전기버스2
# 1. 정류장을 기준으로 교체 후 갈 수 있는 경로의 경우
# 2. 배터리 잔량 기준으로 갈 수 있는 경로의 경우

def f(stn, tmp, btr):
    i = j = 0
    while i < N:
        for k in range(1, ):
            tmp += 1





T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    stn = [0] + arr[1:]
    tmp = 0         # 현재 위치
    btr = 0
    f(stn, 0, 0)


