
## 정식이의 은행 업무 dfs
# 3진수 일때 1로 바꿀 떄랑 2로 바꿀 때 dfs
import copy

def dfs(n, arr, k, a, b):       # 바뀐 자리수(순서대로 바꿔가줄거임). 원래 숫자 배열, k진수
    if n == len(arr):
        return                  # (3 ≤ 2진수, 3진수의 자릿수 <40) == (num2 >=4 and num3 >=9)

    arr2 = copy.deepcopy(arr)
    if arr2[n] == a:        # a이면 b로
        arr2[n] = b


    if k == 2:       # 2진수면
        sum = 0
        for i in range(len(arr2)):
            sum += arr2[i] * (k ** (len(arr2) - 1 - i))
        if sum >= 4:
            set2.add(sum)
    elif k == 3:
        sum = 0
        for i in range(len(arr2)):
            sum += arr2[i] * (k ** (len(arr2) - 1 - i))
        if sum >= 9:
            set3.add(sum)

    dfs(n + 1, arr, k, a, b)


T = int(input())
for t in range(1, T+1):
    num2 = list(map(int, input()))
    num3 = list(map(int, input()))
    set2 = set()
    set3 = set()
    dfs(0, num2, 2, 0, 1)
    dfs(0, num2, 2, 1, 0)

    dfs(0, num3, 3, 0, 1)
    dfs(0, num3, 3, 0, 2)
    dfs(0, num3, 3, 1, 0)
    dfs(0, num3, 3, 1, 2)
    dfs(0, num3, 3, 2, 0)
    dfs(0, num3, 3, 2, 1)

    # print(set2)
    # print(set3)
    for n in set2:
        if n in set3:
            ans = n
    print(f'#{t} {ans}')