T = int(input())
for t in range(T):
    
    K, N, M = map(int,input().split())          # K : 최대 이동가능 정류장 수
                                                # N : 총 이동 정류장 수
                                                # M : 충전기 설치 정류장 수
    now = 0
    can_go = now + K                            # 갈 수 있는 정류장 수
    cnt = 0                                         # 충전 횟수
    stations = list(map(int,input().split()))       # 예) [1,3,5,7,9]
    charge_stn = 0                                  # 다음 충전소
    
    while can_go < N:                           # 갈 수 있는 거리가 총 거리보다 작을 때
        for i in stations:                      # 충전기 있는 스테이션마다 
            if now < i <= can_go:               # i = 1 일 때 charge_stn = 1
                charge_stn = i                  # i = 3 일 때 charge_stn = 3  로 갱신 can_go = 3
                                                # 현재 위치보다 앞에, 갈 수 있는 거리보다 작은 지점에 있는 충전소
                                                # 다음 충전소로 갱신
            elif can_go < i:                    # i = 5 갈 수 있는 거리(3)보다 크므로 break 
                break                               # 두번째 turn: i = 5
                                                    # charge_stn = 5 # now = 5 # can_go = 8 # cnt = 2
                                                        # 세번째 turn: i = 7
                                                        # charge_stn = 7 # now = 7 # can_go =10 # cnt = 3
                                                                                                                   
        if charge_stn == -1:                                
            cnt = 0
            break
        now = charge_stn                        # now = 3 으로 갱신
        can_go = now + K                        # can_go = 3 + 3 = 6
        cnt += 1                                # cnt = 1
        charge_stn = -1                         # charge_stn = -1

    print(f'#{t+1} {cnt}')
