# def f(i,k):
#     if i ==k:
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
# A ={1,2,3}
# N = len(A)
# bit = [0] *N
# f(0,N)

'''
2+3*4/5
'''

fn = list(input())
stack = [0] * len(fn)
top = -1
postfix = ''
op = {'*': 2, '/': 2, '+': 1, '-': 1}

for t in fn:
    # 피연산자인 경우
    if '0' <= t <= '9':          # ascii 코드로 받음
        postfix += t
    elif t in op:                # 연산자인 경우
        if top == -1 or op[stack[top]] < op[t]:     # 스택이 비어있거나 토큰의 우선순위가 높으면
            top += 1                                # push
            stack[top] = t
        else:                                       # 스택에 남아있고 토큰의 우선순위가 높을 때까지
            while top > -1 and op[stack[top]] >= op[t]:
                top -= 1
                postfix += stack[top+1]
            top += 1            # push
            stack[top] = t

while top > -1:             # 스택에 연산자가 남아있으면
    top -= 1            # pop
    postfix += stack[top +1]
print(postfix)

