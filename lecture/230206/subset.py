# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

#
# arr = [3,6,7,1,5,4]
# n = len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end = ', ')
#     print()
# # print()


arr = [1, 3, 5, 8]
n = len(arr)    # n : 원소의 개수(4개)

for i in range(1<<n):    # 1<<n : 부분 집합의 개수
    temp = []    # temp : 부분 집합을 저장할 임시 리스트 초기화
    for j in range(n):    # 원소의 수만큼 비트를 비교함
        if i&(1<<j):  #i의 j번째 비트가 1이면 True
            temp.append(arr[j])    # 비트가 1에 해당하는 원소를 부분 집합 리스트에 추가
    print(temp)




