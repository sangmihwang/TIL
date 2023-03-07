def binarySearch(a, N, key):
    start = 0
    end = N - 1
    cnt = 0
    while start <= end:
        middle = (start + end) //2
        if a[middle] == key:        # 검색 성공
            cnt += 1
            break
        elif a[middle] > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    Page = [n for n in range(1, P+1)]
    bA = binarySearch(Page, P, Pa)
    bB = binarySearch(Page, P, Pb)
    if bA < bB:
        print(f'#{t} A')
    elif bA > bB:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')