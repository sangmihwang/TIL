## 1차 시도

T = int(input())
for t in range(T):
    N = int(input())
    A = [0] * 10
    B = [0] * 10
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    P = int(input())
    bus_stop = [input() for _ in range(5)]
    bus_stop_cnt = [0] * P
    for i in range(N):
        for j in range(A[i]-1, B[i]):
            bus_stop_cnt[j] += 1
    
    print(f'#{t+1}', *bus_stop_cnt)

## 2차 시도

T = int(input())
for t in range(T):
    N = int(input())
    A = [0] * 5000
    B = [0] * 5000
    bus_stop = [0] * 5000
    for i in range(N):
        A[i], B[i] = map(int, input().split())    # A = [1, 2] 
                                                  # B = [3, 5] # 1부터 3까지, 2부터 5까지
        

    P = int(input())                            # 4 라면
    want_bus_stop = [input() for _ in range(P)]    # [1,3,4,5]   구하려는 정류장 번호
    bus_stop_cnt = [0] * P                    # [0,0,0,0]   정류장 지나는 버스 수 빈 리스트
    for i in range(N):                      
        for j in range(A[i]-1, B[i]):
            bus_stop[j] += 1                # 전체 정류장 별 지나가는 버스 수 리스트
                                                # [1,2,2,1,1]

    for i in range(len(want_bus_stop)):
        bus_stop_cnt[i] = bus_stop[i]
    

    print(f'#{t+1}', *bus_stop_cnt)                     # 정답 1 2 1 1


## 3차 시도
T = int(input())
for t in range(T):
    N = int(input())
    A = [0] * 5000
    B = [0] * 5000
    bus_stop = [0] * 5000
    for i in range(N):
        A[i], B[i] = map(int, input().split())    # A = [1, 2] 
                                                  # B = [3, 5] # 1부터 3까지, 2부터 5까지
        

    P = int(input())                            # (예시) P = 4 
    want_bus_stop = [int(input()) for _ in range(P)]    # [1,3,4,5]   구하려는 정류장 번호
    bus_stop_cnt = []                               # 정류장 지나는 버스 수 빈 리스트
    for i in range(N):                      
        for j in range(A[i]-1, B[i]):
            bus_stop[j] += 1                        # 전체 정류장 별 지나가는 버스 수 리스트
                                                    # [1,2,2,1,1]

    for i in want_bus_stop:
        bus_stop_cnt.append(bus_stop[i-1])      # 주어진 문제가 우연히 연속된 수여서 가능했으나
                                                # 연속 되지 않았을 경우는 오류
                                                # 연속 되지 않는 정류장의 경우를 위해 append로 바꿔줌
    print(f'#{t+1}', *bus_stop_cnt)                 

