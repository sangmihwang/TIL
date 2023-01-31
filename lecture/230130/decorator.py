

def decorator(func):
    def wrapper():
        print('함수 시작')
        func()
        print('함수 끝')
    return wrapper


@decorator
def func3():
    print('func3')

func3()