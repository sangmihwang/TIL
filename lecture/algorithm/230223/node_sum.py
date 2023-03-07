def postorder(i, N):             # 후위순회
    if i <= N:
        if tree[i] == 0:         # leaf가 아니면
            r1 = postorder(i*2, N)
            r2 = postorder(i*2 + 1, N)
            tree[i] = r1 + r2
        return tree[i]
    else:
        return 0

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())  # N 노드 개수, M 리프 노드 개수, L 출력 노드 번호
    lst = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N+1)          # 노드 번호 인덱스로 값을 완전이진트리에 저장

    for i in range(M):
        idx, num = lst[i][0], lst[i][1]        # (리프노드번호, 값)
        tree[idx] = num

    postorder(1, N)
    print(f'#{t} {tree[L]}')