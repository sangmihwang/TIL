def f(i, k, s, t):              # i 원소, k 집합의 크기, s i-1까지 고려된 함
    global cnt
    global fcnt
    fcnt += 1
    if s > t:
        return
    elif s == t:
        cnt += 1
        return
    elif i == k:
        if s ==t:
            cnt += 1
            return
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end = ' ')
        print()

        return
    else:
        bit[i] = 1
        f(i+1, k, s + A[i], t)      # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)             # A[i] 미포함

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
cnt = 0
bit = [0]*N


