# def reverse(list):
#     r_list = []
#     for i in range(len(list)):
#         r_list.append(list[-(i+1)])
#     return r_list

T = int(input())

arr = [input() for _ in range(100)]
# r_arr = [[0] * 100 for _ in range(100)]     # arr을 상하/좌우대칭
# print(arr[1])
for t in range(1, T+1):                     # 가로
    for i in range(100):                    # 100개의 리스트로
        cnt = 0
        w = 99
        for j in range(100):
            for a in range(99):
                for b in range(99):
                    if arr[i][j+a] == arr[i][w-b]                    # arr[i]에서




            for a in range(99, 0, -1):
                while arr[i][j] == arr[i][a]:
                    cnt += 1
    print(cnt)



    #
    #         r_arr[i][j] = arr[99-i][99-j]
    # for i in range(100):
    #     for j in range(100):
    #         for a in range(99-j):
    #             if arr[i][j:j+a] == r_arr[i][j+a]:









# for tc in range(1, 11):
#     tc = int(input())
# N = 100
# result = 1
#
# # 가로줄 확인
# Garo_lst = []
# for i in range(N):
#     Data = input()
# Garo_lst.append(Data)
# # 회문 길이
# for M in range(N, result, -1):
#     if
# result > M:
# break
# for k in range(N - M + 1):
#     if Data[k:M + k] == Data[k:M + k][::-1]:
#         if len(Data[k:M + k]) > result:
#             result = len(Data[k:M + k])


