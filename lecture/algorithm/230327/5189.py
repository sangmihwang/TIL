def perm(i, k):
    if i == k:
        lst.append(p)
    else:
        for j in range(k):  # 사용하지 않은 숫자를
            if used[j] == 0:    # used에서 순서대로 검색
                p[i] = A[j]
                used[j] = 1     # j번 자리 숫자 사용으로 표시
                perm(i+1, k)
                used[j] = 0     # j번 자리 숫자를 다른 자리에서 쓸 수 있게
    return(lst)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    A = []
    for a in range(1, N+1):
        A.append(a)
    lst = []
    p = [0] * N
    used = [0] * N
    print(perm(0, N))
