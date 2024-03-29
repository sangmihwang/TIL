def msort(s, e):
    if s == e:
        return
    m = (s+e)//2
    msort(s, m)
    msort(m+1, e)
    k = 0
    l, r = s, m+1       # 왼쪽과 오른쪽에서 가장 작은 인덱스
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1
    i = 0
    while i < k:                # 복사본 내용 원래 리스트에 정렬
        arr[s+i] = tmp[i]
        i += 1
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N           # 복사본 생성성
    msort(0, N-1)
    print(arr)