# 가위바위보 게임 틀 구현

# 필요한 변수 선언 (가위바위보 리스트, 유저/컴퓨터 승 카운트, 판 수)
li =['가위', '바위', '보']
computer_win_count = 0
user_win_count = 0
game = 1

print("가위바위보 게임을 시작합니다!")
menu = int(input('메뉴를 선택하세요 (1: 게임하기, 2: 종료하기): '))

# 종료하기를 입력하거나 5판을 하기 전까지 무한 반복
while True:
    # 5판 후에는 반복문 종료
    if game == 6:
        break
    
    # 게임하기
    if menu == 1:
        game += 1
        pass
    
    # 종료하기
    elif menu == 2:
        print('프로그램을 종료합니다')
        pass
    
    # 그 외 값 입력
    else:
        print("똑바로 입력하십쇼")
        continue
    break
    
for game in range(1,6):
    user = int(input("어떤 것을 내실래요? (1: 가위 / 2: 바위 / 3: 보): "))
    if user < 2:
        computer_win_count += 1
        print('컴퓨터의 승리!')
        print('현재 컴퓨터:', computer_win_count, '승 / 유저:', user_win_count, '입니다') 

   