for t in range(1, 11):
    lst, start = map(int, input().split())
    ppl = list(map(int, input().split()))
    line = [[0] * (max(ppl)+1) for _ in range(max(ppl))]

    for i in range(lst//2):
        n = 0
        if not line[n][ppl[i * 2]]:             # 0이면 그대로 적고
            line[n][ppl[i * 2]] = [ppl[i * 2 + 1]]
        else:                                   # 0 아니고 다른 숫자 있으면
            while line[n][ppl[i * 2]]:
                n += 1                              # 다음 칸에 적음
            line[n][ppl[i * 2]] = [ppl[i * 2 + 1]]


