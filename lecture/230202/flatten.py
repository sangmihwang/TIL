for t in range(10):

    N = int(input())
    box = list(map(int, input().split()))
    maxBox = 0
    minBox = 100
    

    # box[50] = 99  maxbox = 99
    for i in range(N):
        j_max = 0
        j_min = 0
        for j in range(len(box)):        # box 놓인 구간 길이만큼 반복
            if box[j] > maxBox:
                maxBox = box[j]
                j_max = j
                
            if box[j] < minBox:
                minBox = box[j]
                j_min = j
        box[j_max] -= 1
        box[j_min] += 1 
    
    

            
    print(f'#{t+1} {box[j_max]-box[j_min]}')
            
