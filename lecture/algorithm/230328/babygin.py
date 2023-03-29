def f(lst):
    global ans
    for i in range(len(lst)):
        if lst[i] >= 3:          # triplet
            ans = 1
        if lst[i] >= 1 and lst[i+1] >= 1 and lst[i+2] >= 1:     # run
            ans = 1


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    A = [0]*12
    B = [0]*12              # index range 맞춰주려고 2 더함
    ans = 0
    win = 0
    for i in range(6):
        A[arr[i*2]] += 1
        f(A)
        if ans:
            win = 1
            break

        B[arr[i*2+1]] += 1
        f(B)
        if ans:
            win = 2
            break

    print(f'#{t} {win}')




# [9, 5, 5, 1, 4, 2]
# [9, 6, 6, 1, 2, 1]
# [5, 2, 1, 2, 9, 0]
# [3, 9, 5, 0, 2, 0]
#
# [2, 7, 0, 2, 5, 0]
# [8, 7, 2, 2, 4, 3]