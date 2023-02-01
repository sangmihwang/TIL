a = 0

# Enclosed
def func1() :
    a = 10

    # Local
    def func2():
        a = 20
        print(a)
    
    func2()   # 20
    print(a)  

func1()   # 10
print(a)  # 0


# 아스키코드

a = 'a'

for i in range(26):
    print(ord('A') + i, end =' ')


# ord: 문자 -> 숫자
# chr: 숫자 -> 문자

w = input()

# 소문자 알파벳 ( 97 ~ 123 )
if 97 <= ord(w) <= 123:
    print('소문자 알파벳이다')