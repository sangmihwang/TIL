for t in range(1, 11):
    T = int(input())
    num = list(map(int, input().split()))
    ans = False
    while True:
        for i in range(1, 6):
            n = num.pop(0) - i
            if n <= 0:
                n = 0
                ans = True
            num.append(n)
            if ans:
                break
        if ans:
            break
    print(f'#{t}', *num)
