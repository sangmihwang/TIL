T = int(input())
for t in range(T):
    N = int(input())
    bus_stop = [0] * 1001     # 버스 정류장 번호 순서대로 정차 버스 수
    	
    for j in range(N):
        bus_line_stop = list(map(int,input().split()))  # [버스타입, 시작, 끝]
        
        if bus_line_stop[0] == 1:       # 1 일반 버스일 때 지나는 모든 정류장
            for i in range(bus_line_stop[1], bus_line_stop[2]+1):
                bus_stop[i] += 1
        
        if bus_line_stop[0] == 2:       # 2 급행일 때 시작점 홀수면 홀수만, 짝수면 짝수만
            for i in range(bus_line_stop[1], bus_line_stop[2], 2):
                    bus_stop[i] += 1
            
            bus_stop[bus_line_stop[2]] += 1     # 끝 정류장 무조건 포함

        if bus_line_stop[0] == 3:       
            bus_stop[bus_line_stop[1]] += 1     # 시작 정류장 무조건 포함
                                                # 3 광역 급행일 때 시작점 짝수면 4배수만
            if bus_line_stop[1] % 2 == 0:       # 홀수면 3배수면서 10배수 아닌 정류장 
                for i in range(bus_line_stop[1] + 1, bus_line_stop[2]):
                    if i % 4 == 0:
                        bus_stop[i] += 1

            else:
                for i in range(bus_line_stop[1] + 1, bus_line_stop[2]):
                    if i % 3 == 0 and (i % 10 != 0):
                        bus_stop[i] += 1
            
            bus_stop[bus_line_stop[2]] += 1     # 끝 정류장 무조건 포함
    
    
    print(f'#{t+1}', max(bus_stop))



                                                   

            




