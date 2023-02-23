import sys

N = int(sys.stdin.readline())
stack = []

def push(v):
    stack.append(v)
def pop():
    if stack:
        return stack.pop()
    else:
        return -1
def size():
    return len(stack)
def empty():
    if not stack:
        return 1
    else:
        return 0
def top():
    if stack:
        return stack[-1]
    else:
        return -1


for i in range(N):
    func = sys.stdin.readline().split()    # map(input()) 으로 받았더니 계속 시간초과 뜸
    
    if len(func) == 2:  
        push(int(func[1]))
    else:
        if func[0] == "top":
            print(top())
        elif func[0] == "size":
            print(size())
        elif func[0] == "empty":
            print(empty())
        elif func[0] == "pop":
            print(pop())





