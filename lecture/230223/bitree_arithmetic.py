def f(i):
    if tree[i] not in ['+', '-', '*', '/']:     #tree[i]가 피연산자면
        return tree[i]
    else:
        r1 = f(left[i])
        r2 = f(right[i])
        if tree[i] == '+':
            return r1 + r2
        elif tree[i] == '-':
            return r1 - r2
        elif tree[i] == '*':
            return r1 * r2
        elif tree[i] == '/':
            return r1 // r2

for t in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)            # 트리의 데이터 저장, 연산자 또는 피연산자
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        idx = list(input().split())
        if len(idx) > 2:            # 연산자 포함 리스트
            tree[int(idx[0])] = idx[1]
            left[int(idx[0])] = int(idx[2])
            right[int(idx[0])] = int(idx[3])
        else:
            tree[int(idx[0])] = int(idx[1])

    print(f'#{t} {f(1)}')
