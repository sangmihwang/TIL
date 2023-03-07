import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드의 수
    parent = [0] * (N + 1)  # 각 노드의 부모 저장
    for _ in range(N - 1):
        i, j = map(int, input().split())
        parent[j] = i
    # print(parent) [0, 8, 10, 16, 8, 8, 4, 6, 0, 5, 4, 10, 16, 1, 1, 6, 10]
    a, b = map(int, input().split())
    a_parents, b_parents = [0, a], [0, b]  # index 맞춰주려고 0 시작
    while parent[a]:
        a_parents.append(parent[a])
        a = parent[a]
    while parent[b]:
        b_parents.append(parent[b])
        b = parent[b]
    # print(a_parents) [0, 16, 10, 4, 8]
    # print(b_parents) [0, 7, 6, 4, 8]

    i = 1
    while a_parents[-i] == b_parents[-i]:  # 달라지는 순간까지 카운트
        i += 1

    print(a_parents[-i + 1])