T = int(input())
for t in range(1, T+1):
    str1 = input()                              # 문자열 리스크말고 그대로 받아도
    str2 = input()                              # 순서 []안에 쓸수 있음
    ans = 0                                            # 원래 else로 뒤에 썼었는데
    for i in range(len(str2)- len(str1) +1):            # 그렇게 되니까 자꾸 아닐때
            if str2[i:i+len(str1)] == str1:             # 0으로 ans 값 초기화됨
                ans = 1

    print(f'#{t} {ans}')






