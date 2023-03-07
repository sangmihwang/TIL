T = int(input())
for t in range(1, T+1):
    num = list(n for n in input())
    mir = [0] * len(num)
    for n in range(len(num)):
        if num[n] == 'b':
            mir[len(num)-1 - n] = 'd'
        if num[n] == 'd':
            mir[len(num)-1 - n] = 'b'
        if num[n] == 'p':
            mir[len(num)-1 - n] = 'q'
        if num[n] == 'q':
            mir[len(num)-1 - n] = 'p'
    mir = "".join(mir)

    print(f'#{t}', mir)

