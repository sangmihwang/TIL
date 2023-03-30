def f(i, k, s, key):
    global cnt
    if i == k:
        if s == key:
            print(bit)
            cnt += 1

    else:
        bit[i] = 0
        f(i+1, k, s, key)
        bit[i] = 1
        f(i+1, k, s+A[i], key)

A = [i for i in range(1, 11)]
N= 10
bit = [0] * 10
key = 10
cnt = 0
c = 0
f(0, N, 0, key)
print(cnt, c)