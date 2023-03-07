def inorder(n):
    global cnt
    if n <= N:
        inorder(n*2)             # 왼쪽 자식으로 들어와서 전개
        tree[n] = cnt           # 트리 번호에 중위 순회로 이동한 횟수 저장
        cnt += 1
        inorder(n*2 + 1)         # 오른쪽 자식으로 들어와서 전개

for t in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)              # 트리 인덱스 번호 리스트에다 노드 값 넣을거임
    cnt = 1
    inorder(1)                     # 1부터 시작

    print(f'#{t} {tree[1]} {tree[N//2]}')