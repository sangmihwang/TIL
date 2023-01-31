n = int(input())
func = str(input())
if func.split(' ')[0] == "push":
    func1 = func.split(' ')[0]
    func2 = func.split(' ')[1]
else:
    pass

class Stack:
    def __init__(self):
        self.items = []
    def push(self, v):
        self.items.append(v)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1
s = Stack()

for i in range(n):
    if func1 == "push":
        s.push(int(func2))
    elif func == "top":
        print(s.top())
    elif func == "size":
        print(s.size())
    elif func == "empty":
        print(s.empty())
    elif func == "pop":
        print(s.pop())





