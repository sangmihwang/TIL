# N = 3
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             for l in range(1, P+1):
#                 ni = i + di[k] * l
#                 nj = j + dj[k] * l
#                 if 0 <= ni < N and 0 <=nj < N:
#                     print(i, j, ni, nj)


# i : 행의 좌표 , len(arr)
# j : 열의 좌표 , len(arr[0])
arr = [[1,2,3], [4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)