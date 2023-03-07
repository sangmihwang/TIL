
# map(function, iterable)

numbers = [1, 2, 3]
result = map(str, numbers)
lst = list(result)
print(result, type(result), lst)


# n, m = map(int, input().split())
# print(n, m)

# filter(function, iterable)
# 순회 가능한 데이터구조의 모든 요소에 함수 적용하고, 
# 그 결과가 True인 것 filter object로 반환

def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
print(list(result))


def odd(n):
    return [x for x in range(n) if x % 2]

print(odd(5))


# zip(*iterables) 

girls = ['jane', 'ashley']
boys = ['justin', 'eric', 'zach']  # 갯수 안 맞으면 뒤에꺼 생략됨
pair = zip(girls, boys)
print(pair, type(pair))
print(list(pair))


# lambda 함수
# lambda[parameter] : 표현식

# def triangle_area(b, h):
#     return 0.5 * b * h
# print(triangle_area(5, 6))

# 삼각형의 넓이를 구하는 공식 - 람다
triangle_area = lambda b, h : 0.5 * b * h
print(triangle_area(5, 6))


# 재귀함수
# 자기 자신을 호출하는 함수

def fac(n):
    if n == 0:
        return 1  # 꼭 끝나는 지점 명시해줘야
    return n * fac(n - 1)

print(fac(5))
print(fac(1))
print(fac(0))


# 패킹

