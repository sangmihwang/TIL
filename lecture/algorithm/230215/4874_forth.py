T = int(input())
op = {'*': 2, '/': 2, '+': 1, '-': 1}

for t in range(1, T+1):
    fn = list(input().split())
    fn = fn[:-1]                        # 마지막 점 제외
    stack = []

    for i in fn:
        if i in op:
            if len(stack) >= 2:         # pop할 게 두개 이상 있어야
                n2 = stack.pop()
                n1 = stack.pop()
                if i == '*':
                    n3 = n1 * n2
                elif i == '/':
                    n3 = n1 // n2
                elif i == '+':
                    n3 = n1 + n2
                elif i == '-':
                    n3 = n1 - n2
            else:                       # pop할 수 2개 없으면 error
                ans = 'error'
                break
            stack.append(n3)
        else:                                # 피연산자인 경우
            stack.append(int(i))

        if len(stack) == 1:                 # stack에 숫자 하나만 있어야 에러 아님
            ans = stack[0]
        else:
            ans = 'error'
    print(f'#{t} {ans}')


