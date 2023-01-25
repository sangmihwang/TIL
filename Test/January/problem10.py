# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = position[0] 
    b = position[1] 
    if M == 0:
        position = (a-1, b)
    elif M == 1:
        position = (a+1, b)
    elif M == 2:
        position = (a, b-1)
    else:
        position = (a, b+1)
    
    if position[0] < 0 or position[1] < 0 or position[0] > N-1 or position[1] > N-1:
        return('False')
    else:
        return('True')
    
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
