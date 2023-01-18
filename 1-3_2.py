li = [1,2,3,4]

def func():
    li = [5,6,7]
    print(li)

func()
print(li)


def func1():
    x = 10

    def func2():
        nonlocal x

        x = 20
    func2()
    print(x)

func1()
print(x)
