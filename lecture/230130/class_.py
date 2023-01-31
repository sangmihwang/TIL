# 클래스, 인스턴스
# 인스턴스 변수, 클래스 변수
# 매직 메서드 개념, 재정의
# 인스턴스 메서드, 클래스 메서드, 스태틱 메서드
class Nationality:
    count = 0

    def __init__(self, nationality, population):
        self.nationality = nationality
        self.population = population
        Nationality.count += 1

    def __del__(self):
        Nationality.count -= 1

    # 인스턴스 메서드
    # 인스턴스 레벨에서 사용함
    #  -> 인스턴스가 가진 데이터를 다룬다
    # 클래스 변수, 인스턴스 변수 모두 사용 가능

    def get_population(self):
        print(f'{self.nationality} - {self.population}')


    # 클래스 메서드
    # 클래스 변수만 사용가능한 메서드 - 인스턴스 변수 사용 시 에러
    @classmethod
    def get_count(cls):
        print(f'전체 나라 수는 {cls.count} 입니다')

    # 둘 다 아닌 경우
    #  -> 인스턴스 변수, 클래스 변수 모두 사용하지 않는 메서드
    # 변수는 안 써도 문맥 상 해당 클래스에 포함된다고 판단될 때

    @staticmethod
    def print_test():
        print('print_test')

    def __str__(self):
        return '나의 국적은 ' + self.nationality

# static method는 클래스 밖에서 선언해도 전혀 문제 없으며 동작도 동일
def print_test():
        print('print_test')

korea_nationality = Nationality("대한민국", 5174)
use_nationality = Nationality("미국", 33190)
china_nationality = Nationality("중국", 141200)

korea_nationality.get_population()
Nationality.get_count()

del china_nationality

    