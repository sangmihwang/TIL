#  람다 함수
li = [1, 4,2,3,4,2]

#  원본 함수를 변경시켜줌
li.sort()
li.sort(reverse = True)
#  정렬된 함수를 반환시켜줌
new_li = sorted(li)


# 코드가 짧고 단순하다
# 다른 곳에서 안 쓰인다 (일회용)
# 람다 함수(익명 함수)의 특징
li = [[9, "가"], [2, "바"], [7, "다"], [5, "나"]]

# def func(x):
#     return x[1]
   
# li.sort(key = func)
li.sort(key = lambda element: element[1])

print(li)


arr1 = [1,2,3]
arr2 = arr1
arr1.append(4)
print(arr2)


