
## Binary Counting으로 부분집합 생성하기

arr = [3,5,2,8,1,7]
n = len(arr)

for i in range(0, (1<<n)):  # 모든 부분집합의 개수만큼
    for j in range(n):  # 원소 수만큼 비트를 비교
        if i & (1<<j):      # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end='')      # 하나 쓰고 줄바꿈되는것 막기 위해
    print()             # 한 포문 완료 되면 줄 바꿈
