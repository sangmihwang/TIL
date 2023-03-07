class Goblin:
    def __init__(self, hp):
        self.hp = hp

    def attack(self):
        print("몽둥이를 휘두른다")

    def avoid(self):
        print("공격을 회피했다")

class Stone_Goblin(Goblin):  # Goblin 줌으로써 Goblin의 기능 다 가져옴
    # 부모와 다른 동작을 하는 메서드 (재정의 - 오버라이딩)
    def attack(self):
        print("돌을 던진다")
    
    # 부모와 완벽히 동일한 동작하는 메서드는 생략가능
    # def __init__(self, hp):
    #     self.hp = hp

    # def avoid(self):
    #     print("공격을 회피했다")

class IceGoblin(Goblin):
    def __init__(self, hp, mp):
        # 부모와 동일
        # self.hp = hp
        # 부모와 동일한 속성 -> super를 사용하여 부모의 생산자를 호출
        super().__init__(hp)

        # 자식에게만 있는 속성
        self.mp = mp

    def attack(self):
        print("돌을 던진다")

    def skill(self):
        print("얼음돌을 던진다")



# s1 = Goblin(20)  # hp = 20
# s1.attack()

s1 = Stone_Goblin(20)
s1.attack()