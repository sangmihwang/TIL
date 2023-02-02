for t in range(10):

    N = int(input())
    box = list(map(int, input().split()))
    maxBox = 0
    minBox = 100


    for i in range(N):
        j_max = 0
        j_min = 0   
        maxBox = 0
        minBox = 100
        for j in range(len(box)):
            if box[j] >= maxBox:
                maxBox = box[j]
                j_max = j
            
            if box[j] <= minBox:
                minBox = box[j]
                j_min = j
                
        box[j_max] -= 1        
        box[j_min] += 1 

    m = 0
    n = 100
    for w in range(len(box)):
        if box[w] > m:
            m = box[w]
        if box[w] < n:
            n = box[w]

    print(f'#{t+1} {m-n}')


            
