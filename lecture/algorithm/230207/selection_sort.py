'''
7
7 2 5 3 4 6 4
'''
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# for i in range(N-1):  # 작업 구간의 시작 인덱스
#     minIdx = i        # 맨 앞이 최소라 가정
#     for j in range(i+1, N):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[minIdx], arr[i] = arr[i], arr[minIdx]
# print(arr)

def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i                      # 인덱스 0부터
        for j in range(i+1, N):         # 주어진 i번째 다음 인덱스부터
            if a[minIdx] > a[j]:        # minIdx번째 수보다 j번째 수가 작으면
                minIdx = j              # 최소 인덱스를 j로 바꿈
        a[i], a[minIdx] = a[minIdx], a[i]
    return a

A = [4,6,8,2]
print(selectionSort(A,4))


## Selection Algorithm

def select(a, k):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, len(a)):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    return a[k-1]

print(select(A, 3))