T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())        # 세로 N, 가로 M
    arr = [input() for _ in range(N)]
    code = []

    # 16진수를 2진수로 변환
    for a in arr:
        for i in range(len(a)):
            if a[i] != '0':
                code.append(a)              # code: 암호코드(16진수)
    code = list(set(code))                  # 배열에 있는 모든 암호코드
    code_16 = []                            # code_16: 암호코드(16진수) 리스트

    for i in range(len(code)):
        for j in range(len(code[i])):
            if code[i][j] != '0':
                start = j
                break
        for k in range(len(code[i])-1, 0, -1):
            if code[i][k] != '0':
                end = k
                break
        code_16_u = code[i][start:end+1]      # 앞뒤로 0아닌 곳에서 시작하고 끝나게 지정
        code_16.append(code_16_u)

    code_2 = []
    for i in range(len(code_16)):
        c = int(code_16[i], 16)                 # c: 암호코드(10진수)
        c_2 = bin(c)                             # code_2: 암호코드(2진수)
        c_2_r = str(c_2)[2:]
        code_2.append(c_2_r)
    # print(code_2)

    code_2_1 = []                               # 끝에 0 제거
    for i in range(len(code_2)):
        for j in range(len(code_2[i])-1, 0, -1):
            if code_2[i][j] == '0':
                continue
            else:
                code_2_1.append(code_2[i][:j+1])
                break
    # print(code_2_1)

    # 56개 단위로 맞추기 (앞에 0 추가해서)
    c_56k =[]
    for c in code_2_1:
        add = len(c) % 56
        for i in range(56-add):
            c = '0' + c
        c_56k.append(c)
    print('c_56:',c_56k)

    # 1:1 배율의 암호패턴 찾기
    count = [[0 for _ in range(100)] for _ in range(len(c_56k))]      # 암호코드 개수만큼 0과1 개수 카운트할 리스트 생성
    for k in range(len(c_56k)):                      # 곱하기로 하면 얕은 복사 되어서 리스트가 다 똑같아지므로 for _ range로 해야함
        j = 0
        count[k][j] = 1
        for i in range(len(c_56k[k])-1):
            if c_56k[k][i] == c_56k[k][i+1]:   # 모든 암호는 0부터 시작. 같은 수 연속이면
                count[k][j] += 1               # 같은 수면 count 인덱스 안옮기고 횟수만 추가
            else:                           # 앞에랑 다른 수면
                j += 1                      # 인덱스 다음으로 넘겨주고
                count[k][j] += 1               # 다음 인덱스에 횟수 추가
    print('count:', count)                        # 연속된 0과 1 개수 리스트로 (count는 int)

    for i in range(len(count)):
        r = 100
        for idx in count[i]:
            if count[i][idx] < r and count[i][idx] != 0:
                r = count[i][idx]
        for idx in count[i]:
            count[i][idx] // r

    print(count)




    # 배율 적용된 암호패턴 찾기 (제일 작은 수로 나누어줌)
