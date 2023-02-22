def inorder(i, N):
    if i <= N:
        inorder(2*i, N)             # 왼쪽으로 들어가서 전개
        tree.append(i)
        inorder(2*i + 1, N)         # 오른쪽으로 들어가서 전개
    else:
        return

for t in range(1, 11):
    N = int(input())
    dic = {}                        # {노드 번호: 문자} 딕셔너리 저장
    for i in range(N):
        letter = list(input().split())
        dic[int(letter[0])] = letter[1]     # 첫번째 값과 두번째 값만 취함

    tree = []
    inorder(1, N)
    ans = ''

    for x in tree:
        ans += dic[x]

    print(f'#{t}', ans)