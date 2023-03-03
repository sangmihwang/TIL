def solve(arr):
    str = ''
    for j in range(15):
        for i in range(5):
            try:
                str += arr[i][j]
            except IndexError:
                continue
    return str

T = int(input())
for t in range(1, T+1):
    arr = [list(i for i in input()) for _ in range(5)]

    print(f'#{t} {solve(arr)}')