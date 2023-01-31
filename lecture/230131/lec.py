# class Person:
#     def __init__(self):
#         self.age = 0


#     @property
#     def age(self):   # getter
#         return self._age

#     @age.setter
#     def age(self, age):   # setter
#         self._age = age
    
#     # age = property(get_age, set_age)

# p1 = Person()
# p1.age = 25
# print(p1.age)

# p1._age = 25  # 이거 안됨
# print(p1._age)  # 이거 안됨

# 불편함
# p1.set_age(25)
# print(p1.get_age())


class Rectangle:
    count = 0  # 클래스 변수
 
    # 생성자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count += 1
        
 
    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area



print(Rectangle(2, 5).calcArea())


class Date:
    word = 'date:'

    def __init__(self, date):
        self.date = self.word + date

    @staticmethod
    def now():
        return Date("today")

    def show(self):
        print(self.date)

a = Date("2016.9.13")
a.show()

Date("2015.3.15").show()

b = Date.now()
b.show()
