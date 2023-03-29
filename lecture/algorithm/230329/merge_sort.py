
## SWEA 5204 병합 정렬

def msort(s, e):
    global cnt
    if s == e:
        return
    m = (s+e)//2
    msort(s, m)             # 반 나눠서 왼쪽
    msort(m+1, e)           # 반 나눠서 오른쪽
    k = 0
    l, r = s, m+1           # 각 리스트에서 가장 작은 인덱스
    while l <= m or r <= e:
        if l <= m and r <= e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
                cnt += 1
            k += 1
        elif l <= m:
            while l <= m:
                tmp[k] = arr[l]
                k += 1
                l += 1
        elif r <= e:
            while r <= e:
                tmp[k] = arr[r]         # tmp는 그냥 임시 리스트다
                k += 1                  # 해당 구역의 숫자를 크기 순서대로 잠시 저장
                r += 1
    i = 0
    while i < k:
        arr[s+i] = tmp[i]
        i += 1
    return



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    tmp = [0]*N
    msort(0, N-1)
    print(arr)
    print(f'#{t} {arr[N//2]} {cnt}')

