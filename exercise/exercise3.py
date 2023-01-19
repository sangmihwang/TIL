# fn_d(n)은 n의 제네레이터

def fn_d(n):
    a = list(map(int, str(n)))
     # print(a)
    s = sum(a)
     # print(sum(a))
    return int(n) + s

print(fn_d(91))

# 제네레이터가 없는 숫자는 셀프 넘버

def is_selfnumber(n):
    if fn_d(n)


# fn_d(n)은 n의 제네레이터
fn_d= lambda n: sum([int(c) for c in str(n)] + [n])

print(fn_d(91))

def self_number(n):
    return len([i for i in range(n) if fn_d(i) == n]) == 0

print(self_number(20))


# 소금물 농도와 양 구하기

# mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done







# 출력 예시
# 4.0% 700.0g