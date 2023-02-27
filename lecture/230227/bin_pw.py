num = {'0':'0001101','1':'0011001','2':'0010011','3':'0111101','4':'0100011','5':'0110001','6':'0101111','7':'0111011','8':'0110111','9':'0001011'}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())    # 세로 N, 가로 M
    code = [input() for _ in range(N)]
    pw = ''
    for c in code:
        for i in range(len(c)):
            if c[i] == '1':             # 1이 나오는 곳 암호로 놓고 시도
                pw = c                  # 56자리 포함 수

    for i in range(M-1, 0, -1):               # 뒤에서부터 오다가 1이면
        if pw[i] == '1':
            pw = pw[i-55:i+1]                 # pw 56자리로 지정
            break                # break를 안해줘서 계속 for문을 돌아서 범위가 자꾸 나간다고함ㅜㅜ두시간 고민함 이걸로

    pw_lst = []                 # 비트로 된 암호코드
    for i in range(0, 56, 7):
        pw_lst.append(pw[i:i+7])

    code_lst = []
    for idx in pw_lst:
        for key, value in num.items():
            if value == idx:
                code_lst.append(int(key))         # 키값 code_lst에 저장
    ck = 0
    for i in range(0, 4):
        ck += (code_lst[i*2]*3 + code_lst[i*2+1])

    if ck % 10 == 0:
        ans = sum(code_lst)
    else:
        ans = 0

    print(f'#{t} {ans}')

