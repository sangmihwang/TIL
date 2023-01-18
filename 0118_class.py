a = 0

# Enclosed
def func1() :
    a = 10

    # Local
    def func2():
        a = 20
        print(a)
    
    func2()
    print(a)

func1()
print(a)


# 아스키코드

a = 'a'

for i in range(26):
    print(ord('A') + i, end =' ')