
def hoare(A, l, r):     # 파티션 구하는 함수
    pivot = A[l]        # 맨 왼쪽원소 기준
    i = l               # 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r               # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:       # 교차하지 않은 경우
                        # j보다 오른쪽은 다 크고 i 보다 왼쪽은 다 작으니까
                        # 마지막에 하나 다하기 전에 멈췄을 경우
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]     # 피봇원소 위치확정(교차지점)
    return j

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)

# import sys
# sys.stdin = open('input_m.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N           # 복사본 생성성
    qsort(arr, 0, N-1)
    print(f'#{t} {arr[N//2]}')
