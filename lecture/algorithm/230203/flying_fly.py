T = int(input())
for t in range(T):

    Dist, A_spd, B_spd, F_spd = map(int, input().split())
    time = Dist/(A_spd + B_spd)             # 두 기차가 만날 때까지 걸리는 시간
    f_run = float(F_spd * time)

    print(f'#{t} {f_run}')


        
