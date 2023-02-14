def f(i, k):
    if i ==k:
        for j in range(k):
            if bit[j]:
                print(A[j], end = ' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)
        bit[i] = 2
        f(i+1, k)
    return

A = [2,3,7,9,8]
N = len(A)
bit = [0]*N