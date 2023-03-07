# 문자열이 주어지면 숫자, 문자, 기호가 몇 개인지 출력하는 함수

def check(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else: symbol_count += 1
    
    # 한 개 값만 return 가능
    return char_count, digit_count, symbol_count

input_str = "123#$%aiden_snow"
char_count, digit_count, symbol_count = check(input_str)
print(f"char: {char_count}, digit: {digit_count}, symbol: {symbol_count}")


sample_list = [11, 22, 33, 55, 66]

# 주어진 리스트에 3번 index에 있는 항목을 제거하고 변수에 할당해주세요

print("original list:", sample_list)

elem = sample_list[3]

print('list after:', sample_list)
print('elem:', elem)

# sample_list의 가장 뒤에 77추가
sample_list.append(77)

# 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해 보세요

print(sample_list)
sample_list.insert(2, elem)
print(sample_list)


my_tuple = (11, 22, 33, 44, 55, 66)


# 주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요
new_tule = my_tuple[3:-1]
print(my_tuple)


scores = [('eng',88), ('sci', 90), ('math', 80)]

def check2(x):
    return x[1]

print(scores)
# scores.sort(key=check2)  # 1번 index 기준으로 정렬
scores.sort(key = lambda x: x[1])
print(scores)



# 리스트 + 함수에서의 복사

# 변수끼리의 복사
# 복사 후 값을 변경해도, 원본 값이 유지 -> 깊은복사
# 주소가 아닌, 값을 복사하는 경우

a = 10
b = a
a = 7
print(b)

# 함수에서 ㅂㄴ수의 복사
def func(num):
    num += 10

n = 10
func(n)
# 만약 깊은 복사가 일어난다면 -> 10 출력
# 만약 얕은 복사가 일어난다면 -> 
print(n)

import copy

# 리스트에서 깊은 복사를 하는 방법 
a = [1,2,[3,4]]

b = copy.deepcopy(a)
b = 10

print(a)
print(b)