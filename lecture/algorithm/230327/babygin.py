def f(i, k):
    global ans
    if i == k:
        if (p[0] == p[1] == p[2]) and (p[3]+2 == p[4]+1 ==p[5]):
            # return 1            # return 을 해줬더니 그대로 아까 하던 j 값 마저 하러 내려감
            ans += 1
        elif (p[0]+2 == p[1]+1 ==p[2]) and (p[3] == p[4] == p[5]):
            # return 1
            ans += 1
        elif (p[0]+2 == p[1]+1 ==p[2]) and (p[3]+2 == p[4]+1 ==p[5]):
            ans += 1            # ㅠㅠ 둘다 triplet 이거나 둘다 run 이어도 babygin
        elif (p[0] == p[1] == p[2]) and (p[3] == p[4] == p[5]):
            ans += 1
    else:
        for j in range(k):
            if used[j] == 0:    # 사용하지 않았으면
                p[i] = nums[j]  # 순열 리스트에 숫자 추가
                used[j] = 1     # 사용했다 바꿔줌
                f(i+1, k)
                used[j] = 0     # 올라갔다 왔으니까 다시 사용 안 한 걸로


T = int(input())
for t in range(1, T+1):
    nums = list(map(int, str(input())))
    p = [0] * 6
    used = [0] * 6
    ans = 0
    f(0, 6)
    if ans:
        print(f'#{t}', 'Baby Gin')
    else:
        print(f'#{t}', 'Lose')

