name_list = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
age_list = [17, 18, 22, 24, 25, 19]

for each in zip(name_list, age_list):
    print(each)

def my_magic_func(n):
    return n * 10

map_obj = map(my_magic_func, [1,2,3])
rlt = list(map_obj)

print(rlt)

map_obj = map(lambda n: n * 10, [1,2,3])
rlt = list(map_obj)

print(rlt)

rlt = ((lambda x: x * x)(4))
print(rlt)

my_func = lambda n: n * 2
print(my_func(2))

def pow(x):
    return x * x

# 자기 자신을 호출하는 함수

def recur():
    print('뿅')
    recur()

recur()

# 자기 자신을 호출하는 함수
# 재귀함수

def fac(n):
    if n == 0:
        return 1  # 꼭 끝나는 지점 명시해줘야
    return n * fac(n - 1)

print(fac(5))
print(fac(1))
print(fac(0))



# 패킹 / 언패킹

def my_sum(a, b, c):
    return a + b + c

num_list = [10, 20, 30]

# rlt = my_sum(num_list[0], num_list[1], num_list[2])

rlt = my_sum(*num_list)  # *가 언패킹
print(rlt)

def test(*values):
    for value in values:
        print(value)

test(1)
test(1, 2)
test(1, 2, 3, 4)

def my_sum(a, *args):
    rlt = 0 
    for value in args:
        rlt += value
    return rlt

print(my_sum(1))  # 0

def my_sum1(a, b , *args):
    rlt = 0 
    for value in args:
        rlt += value
    return rlt


print(my_sum1(1, 2, 3))   # 6


def test(*args, **kwargs):
    print(kwargs, type(kwargs))
    kwargs['name']
    return kwargs

# test(name = 'aiden', age = 21)
test(1, 2, 3, 4, name = 'aiden', age = 21, music = 'IU')


import random

num_list = [1, 2, 3, 4]
random.shuffle(num_list)
print(num_list)

from random import shuffle
num_list = [1, 2, 3, 4]
shuffle(num_list)
print(num_list)





