def enq(n):
    global last
    last += 1               # 마지막 정점 추가
    heap[last] = n
    c = last
    p = c//2                # 부모 < 자식
    while p > 0 and heap[p] > heap[c]:      # 부모가 더 크면
        heap[p], heap[c] = heap[c], heap[p]     # 부모 자식 자리 바꿔라
        c = p               # 교환 후 다시 부모 < 자식 확인
        p = c//2
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))       # 노드 값 순서대로 입력
    last = 0
    heap = [0] * (N + 1)                        # 노드 값 받을 리스트
    for x in arr:
        enq(x)

    c = last
    p = c//2
    s = 0
    while p > 0:
        s += heap[p]                # 마지막 정점의 조상이 가진 값 모두 더하기
        p //= 2

    print(f'#{t} {s}')