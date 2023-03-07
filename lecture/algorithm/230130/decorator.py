

# def decorator(func):
#     def wrapper():
#         print('함수 시작')
#         func()
#         print('함수 끝')
#     return wrapper


# @decorator
# def func3():
#     print('func3')

# func3()

def ko_hello(name):
    print(f'안녕하세요, {name}님!')
    # print('^o^')

def en_hello(name):
    print(f'Hello, {name}!')
    # print('^o^')

def add_emoji(name, func):
    func(name)
    print('^o^')

def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^o^')
    
    return wrapper

def add_tears(func):
    def wrapper(name):
        func(name)
        print('ㅠ.ㅠ')
    
    return wrapper


@add_tears
@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')


ko_hello('aiden')

# add_emoji('aiden', ko_hello)   # 두 함수를 합쳐서 짧게 사용할 수 있게

# # ko_hello('aiden')
# # en_hello('aiden')

# new_func = emoji_decorator(ko_hello)  # 이거 자체가 wrapper 라는 함수
# new_func('aiden')

# emoji_decorator(ko_hello)('aiden')  # 제일 축소한 버전

# emoji_decorator(en_hello)('sangmi')


class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'

my_class = MyClass()
print(my_class.method())  # 인스턴스 메서드
print(MyClass.method(my_class))
print(my_class.classmethod())  # 클래스 자체에서 각 메서드를 호출하는 경우
print(my_class.staticmethod())
MyClass.method()