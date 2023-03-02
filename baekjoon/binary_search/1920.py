# 1920_ 수 찾기

# N = int(input())
# Ns = set(map(int, input().split()))         # list로 받으면 시간 초과남;;
# M = int(input())
# Ms = list(map(int, input().split()))
# for i in Ms:
#     if i in Ns:
#         print(1)
#     else:
#         print(0)

N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))
Ns.sort()

def bin_s(m):               # m: 찾고자 하는 수
    left, right = 0, N-1
    while left <= right:
        mid = (left + right) // 2
        if Ns[mid] == m:
            return True
        if m < Ns[mid]:
            right = mid - 1
        elif m > Ns[mid]:
            left = mid + 1

for m in Ms:
    if bin_s(m):
        print(1)
    else:
        print(0)