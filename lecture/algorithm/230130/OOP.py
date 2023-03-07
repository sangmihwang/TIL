
# 클래스 정의
class Person:
    pass

print(type(Person))

# 인스턴스 생성
person1 = Person()

print(isinstance(person1, Person))  # person1은 Person의 instance
print(type(person1))



class Persons:
    blood_color = 'red'  # 클래스 변수
    population = 100  # 클래스 변수

    def __init__(self, name):
        self.name = name   # 인스턴스 변수
person1 = Persons('지민')
print(person1.name)


# 국적을 출력할 수 있는 클래스 작성
class Nationality:
    # 클래스 변수 영역
    # 클래스 변수: 인스턴스들이 모두 같은 내용을 공유해야할 때 사용
    # 몇 개의 나라가 생성되었는지 저장
    count = 0
    
    # 초기화(생성자)
    def __init__(self, nationality):
        # 인스턴스 변수 선언
        self.nationality = nationality   # 인스턴스 변수와 파라미터. 다른거임 서로.
        # 클래스 변수 접근
        Nationality.count += 1
    
    # 매직 메서드 재정의
    # 재정의: 기존에 있던 함수를 "덮어쓰기"하는 동작
    # print 함수 호출 시
    # 원래 Nationality 객체가 가지고 있는 __str__ 함수가 아닌, 
    # 내가 새로 정의한 __str__를 호출한다
    def __str__(self):
        return '나의 국적은 ' + self.nationality
        # print('str')


korea_nationality = Nationality("대한민국")
print(korea_nationality)  # 나의 국적은 대한민국
print(korea_nationality.__str__())

# 매직 메서드 등 모든 객체의 정보 출력
# 매직 메서드: 특정 상황에 자동으로 호출이 되는 함수
print(dir(korea_nationality))

# korea_nationality = Nationality("대한민국")
usa_nationality = Nationality("미국")
china_nationality = Nationality("중국")
print(korea_nationality)
print(usa_nationality)
print(china_nationality)

# 클래스 변수 접근은 인스턴스, 클래스 둘 모두에서 

print(korea_nationality.count) 
print(korea_nationality.count) 
print(korea_nationality.count) 
# 클래스 자체로 클래스 변수 접근