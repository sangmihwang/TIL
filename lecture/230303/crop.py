T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    crop = 0

    for i in range(N//2+1):
        for j in range(N//2-i, N//2+i+1):
            crop += int(arr[i][j])
    for i in range(N//2+1, N):
        for j in range(N//2-(N-i-1), N//2+(N-i)):
            crop += int(arr[i][j])

    print(f'#{t} {crop}')