# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()  # p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수(unknown)가 출력
p1.talk()  

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)  # Person 클래스의 값이 Kim으로 변경된 것이 아닌
                    # p2 인스턴스의 이름 공간에 name이 Kim으로 저장됨
print(p1.name)
print(p2.name)


class Persons:
    count = 0
    # 인스턴스 변수 설정
    def __init__(self, name, type):
        self.name = name
        self.type = type
        Persons.count += 1

    def eat(self, sound):
        self.sound = sound
        print(self.sound)

person1 = Persons('아이유')
person2 = Persons('이찬혁')

print(Persons.count)


class Meal:
    def hello(self):
        print('안녕')

    def eat(self, food):
        print(f'{food}를 냠냠')

m1 = Meal()
m1.hello()
m1.eat('피자')
m1.eat('치킨')

