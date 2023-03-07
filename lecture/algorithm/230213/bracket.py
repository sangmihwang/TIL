T = int(input())
for t in range(1, T+1):
    text = list(input())
    stack = []
    for tx in text:
        if tx == '(':
            stack.append(tx)
        elif tx == '{':
            stack.append(tx)

        if tx == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(tx)
            else:
                stack.append(tx)

        elif tx == '}':
            if stack:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(tx)
            else:
                stack.append(tx)

    if stack:
        ans = 0
    else:
        ans = 1
    print(f'#{t} {ans}')


