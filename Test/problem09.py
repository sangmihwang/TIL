# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number//2
    return result

def dec_to_bin(num):
    # 종료조건을 먼저 작성
    if num//2 == 0:
        return str(num)
    else:
        # 반복하면서 행해야 될 로직
        # num //= 2

        # 다음으로 넘어간다
        return dec_to_bin(num//2) + str(num%2)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
