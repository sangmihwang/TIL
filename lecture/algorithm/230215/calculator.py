for t in range(1, 11):
    N = int(input())
    fu = list(input())
    num = []
    for f in fu:
        if '0' <= f <= '9':
            num.append(int(f))
        ans = sum(num)
    print(f'#{t} {ans}')

