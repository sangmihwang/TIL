def BFS(s):
    queue = []              # 큐 생성
    queue.append(s)         # 시작점 큐에 삽입
    visited[s] = 0
    while queue:            # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # 큐의 첫번째 원소 반환
        for i in line[t]:
            if not visited[i]:
                queue.append(i)                 # 큐에 넣기
                visited[i] = visited[t] + 1     # n으로부터 1만큼 이동 (이동 횟수)

for t in range(1, 11):
    lst, s = map(int, input().split())          # 연결쌍 수, 시작점
    ppl = list(map(int, input().split()))
    line = [[] for _ in range(101)]             # line[from번호] : [to번호 다]
    visited = [0] * 101                         # 정점의 개수 100개
    for i in range(lst//2):
        line[ppl[i*2]].append(ppl[i*2+1])

    BFS(s)
    a = max(visited)
    max_n = 0
    for i in range(len(line)):
        if visited[i] == a:             # 가장 마지막에 받은사람 중에 제일 높은 번호
            max_n = i

    print(f'#{t} {max_n}')



