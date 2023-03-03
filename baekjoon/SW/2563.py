
## 2563_ 색종이

N = int(input())
pap = [tuple(map(int, input().split())) for _ in range(N)]
arr = [[0] * 100 for _ in range(100)]

for (x, y) in pap:
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)