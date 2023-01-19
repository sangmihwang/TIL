li = [1,2,3,4]

def func():
    li = [5,6,7]
    print(li)

func()
print(li)


def func1():
    x = 10

    def func2():
        x = 20
        
        def func3():
            nonlocal x
            x += 10
            print(x)

        func3()
        print(x)

    func2()
    print(x)

func1()



y = 10
def func(y):
    y += 20
    return y

new_y = func(y)