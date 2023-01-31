

class Stack:
    def __init__(self):
        self.items = []  # 데이터 저장을 위한 리스트
    
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        try:  
            return self.items.pop()
        except IndexError:
            print("None")  # pop할 아이템 없으면 indexError 발생
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("None")
    
    def __repr__(self):
        return self.items
    
    def empty(self):
        return self.__repr__() == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.__repr__())
