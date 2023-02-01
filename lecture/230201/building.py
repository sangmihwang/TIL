for t in range(1, 11):
    N = int(input())
    bd = list(map(int, input().split()))
    s = 0
    for i in range(2, N-2):
        a_min = 255
        for v in range(i-2, i+3):
            if i == v:
                continue
            if bd[i] >= bd[v]:
                a = bd[i] - bd[v]            
                if a < a_min:
                    a_min = a
            else:
                a_min = 0
            
        s += a_min

    print(f'#{t} {s}')
    

        

        

    

