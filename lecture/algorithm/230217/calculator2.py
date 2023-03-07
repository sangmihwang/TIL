# for t in range(1, 11):
#     strn = list(input())
#     stack = []
#     res = ''
#     for s in strn:
#         if '0' <= s <= '9':         # 피연산자 만나면
#             res += s
#         else:
#             if s == '(':
#                 stack.append(s)
#             elif s == '*' or s == '/':
#                 while stack and (stack[-1] == '*' or stack[-1] == '/'):
#                     res += stack.pop()
#                 stack.append(s)
#             elif s == '+' or s == '-':
#                 while stack and stack[-1] != '(':
#                     res += stack.pop()
#                 stack.append(s)
#             elif s == ')':
#                 while stack and stack[-1] != '(':
#                     res += stack.pop()
#                 stack.pop()
#     while stack:
#         res += stack.pop()
#     print(res)

for t in range(1, 11):
    N = int(input())
    strn = list(input())
    stack = []
    res = ''
    for s in strn:
        if '0' <= s <= '9':         # 피연산자 만나면
            res += s
        else:                       # 연산자 만나면
            if s == '*':
                while stack and (stack[-1] == '*'):
                    res += stack.pop()
                stack.append(s)
            elif s == '+':
                while stack:
                    res += stack.pop()
                stack.append(s)
    while stack:
        res += stack.pop()

    for r in res:
        if '0' <= r <= '9':
            stack.append(r)
        elif r == '+':
            r2 = stack.pop()
            r1 = stack.pop()
            ans = int(r2) + int(r1)
            stack.append(ans)
        elif r == '*':
            r2 = stack.pop()
            r1 = stack.pop()
            ans = int(r2) * int(r1)
            stack.append(ans)


    print(f'#{t} {ans}')