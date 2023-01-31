# 과제 7-2

# 클래스 정의
# class Doggy:
#     num_of_dogs = 0
#     birth_of_dogs = 0

#     def __init__(self, name, type):
#         self.name = name   # 인스턴스 변수
#         self.type = type
#         Doggy.num_of_dogs += 1
#         Doggy.birth_of_dogs += 1

#     def __del__(self):
#         Doggy.num_of_dogs -= 1

#     def bark(self):
#         print("멍멍")

#     @classmethod
#     def get_status(cls):   # cls는 Doggy와 똑같음
#         print(f'{cls.birth_of_dogs}, {cls.num_of_dogs}')

# Dog1 = Doggy('미니', '불독')
# Dog1.get_status()
# Dog1.bark()

# del Dog1
# Doggy.get_status()



# 실습 7-1

# class Nationality:
#     def __init__(self, nationality):
#         self.nationality = nationality
        
#     def __str__(self):
#         return '나의 국적은 ' + self.nationality


# korea_nationality = Nationality("대한민국")
# print(korea_nationality) # 나의 국적은 대한민국


# 연습

# class Book:
#     def setData(self, title, price, author):
#         self.title = title
#         self.price = price
#         self.author = author
#     def printData(self):
#         print('제목: ', self.title)
#         print('가격: ', self.price)
#         print('저자: ', self.author)
#     def __init__(self):
#         print('책 객체를 새로 만들었어요')

# b = Book()
# b.setData('누가 내 치즈', '2000원', '미키')
# b.printData()
    

# 실습 7-4

# class fee:
#     def __init__(self, rent, distance):
#         self.rent = int(rent[:-1]) / 10 * 1200
#         self.insurance = (int(rent[:-1]) //30 + 1) * 525
#         self.distance = int(distance[:-2]) * 170 if int(distance[:-2]) <= 100 \
#             else 100 * 170 + (int(distance[:-2])-100) * 170/2
#         print('대여 요금: ', self.rent)
#         print('보험료: ', self.insurance)
#         print('주행 요금: ', self.distance)

# f = fee('50분', '120km')
# # f.setData('50분', '120km')  # __init__을 사용함으로써 지울 수 있게 됨
# f.printData()





# 과제 7-4

class collatz:
    count = 0
    def __init__(self, num):
        self.num = num
        self.find()

    def find(self):
        if self.num % 2 == 0:
            self.num = self.num // 2
        else:
            self.num = self.num * 3 + 1
        
        collatz.count += 1
        
        if collatz.count == 500:
            return    # 루프 종료

        if self.num == 1:
            return
            

        self.find()
        
        
        
collatz(12)
print(collatz.count)