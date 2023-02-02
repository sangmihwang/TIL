def Countin_Sort(arr, temp, counts):
    B = [0] * (len(arr))
    counts = [0] * (10)   # counts = [0, 0, 0 ...]  # 예를 들어 arr = [1,2,3,2,1]

    for i in range(0, len(arr)):
        counts[arr[i]] += 1        # arr 길이만큼 돌릴때 arr의 원소 나올 떄마다 개수 더해줌
                                    # counts = [0,2,2,1]
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]   # counts = [0,2,4,5]
    
    for i in range(len(temp)-1, -1, -1):    # range(4,-1,-1) :4,3,2,1,0
        counts[arr[i]] -= 1             
                                        # counts[arr[4]] = counts[1] = 1
                                        # counts[arr[3]] = counts[2] = 3
                                        # counts[arr[2]] = counts[3] = 4
                                        # counts[arr[1]] = counts[2] = 2
                                        # counts[arr[0]] = counts[1] = 0
                                        # counts = [0,0,2,4]
                                        # 이거 다 하고 다음 넘어가는 거 아니고 하나하나씩인데 다 하고 넘어가는 거로 헷갈림

                                    
        temp[counts[arr[i]]] = arr[i]   # temp[1] = arr[4] = 1
                                        # temp[3] = arr[3] = 2
                                        # temp[4] = arr[2] = 3
                                        # temp = [0,1,0,2,3]
        