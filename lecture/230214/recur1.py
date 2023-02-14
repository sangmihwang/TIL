# def f(i, k):        # i: 복사하려는 인덱스, k 배열의 크기
#     if i == k:
#         print(B)
#     else:
#         B[i] = A[i]
#         f(i+1, k)   # 다음 인덱스를 복사하러 이동
#
# A = [10, 20, 30]
# N = len(A)
# B = [0] * N
# f(0, N)

## 리스트에 해당 값 있는지 확인

def f(i, k, key):
    if i == N:      # 배열의 끝, 검색 실패
        return 0
    elif A[i] == key:   # 성공
        return 1
    else:
        return f(i+1, k ,key)  # 다음 원소로 이동

A = [7, 2, 5, 3, 8, 9]
N = len(A)
key = 3
print(f(0, N, key))
key = 6
print(f(0, N, key))
key = 7
print(f(0, N, key))
