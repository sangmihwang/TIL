# 과제 8-2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Rectangle:
    value = 0
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    # 사각형의 넓이
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)


    # 사각형의 둘레 길이
    def get_perimeter(self):
        return ((self.p2.x - self.p1.x) + (self.p1.y - self.p2.y)) * 2


    # 정사각형 여부 # 정사각형이면 True, 정사각형이 아니면 False를 반환
    # @staticmethod
    def is_square(self):
        return (self.p2.x - self.p1.x) == (self.p1.y - self.p2.y)



p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True