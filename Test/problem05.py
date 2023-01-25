# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calc_lunch_cost(lunch_cost):
    pass
    # # 여기에 코드를 작성하여 함수를 완성합니다.
    # return(lunch_cost.get('이싸피') + 
    # lunch_cost.get('김싸피') +  
    # lunch_cost.get('박싸피') + 
    # lunch_cost.get('최싸피') + 
    # lunch_cost.get('조싸피'))

    sum = 0
    for key in lunch_cost:
        sum = sum + lunch_cost[key]  # 이렇게 하면 키값 아니고 value값 받음
    return sum

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    lunch_cost = {
        '이싸피' : 12000,
        '김싸피' : 30000,
        '박싸피' : 10000,
        '최싸피' : 15000,
        '조싸피' : 18000, 
    }

    print(calc_lunch_cost(lunch_cost))  # 85000