import calendar

# year가 윤년이면 True를, 그렇지 않으면 False를 반환
while True:
    year = int(input())
    if calendar.isleap(year) == True:
        print("윤년입니다. 연도를 다시 입력해주세요.")      
    else:
        # calendar()에서 반환 한 연도 전체 달력을 인쇄
        print(calendar.calendar(year))
        break

month = int(input())
day = int(input())
weekday = calendar.weekday(year, month, day) 

if weekday == 0:
    print("경고 월요일입니다.")
else:
    pass

if weekday == 0:
    weekday = '월요일'
elif weekday == 1:
    weekday = '화요일'
elif weekday == 2:
    weekday = '수요일'
elif weekday == 3:
    weekday = '목요일'
elif weekday == 4:
    weekday = '금요일'
elif weekday == 5:
    weekday = '토요일'
else:
    weekday = '일요일'

dict = {'년': year, '월':month, '일': day, '요일': weekday}
print(dict)









# 애너그램(Anagram)
# sorted 함수
 


def group_anagrams():
    li = list(input())
    
for i,j in range(len(li)):
    if sorted(list[i]) == sorted(list[j]):




if sorted(a) == sorted(b):
    list.append(a)
    list.append(b)
print(list)


# A.    입력 예시 
a = ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


def group_anagrams(a):
    result = {}
    for i in a:
        b=''.join(sorted(i))
        result[b] = result.get(b, []) + [i]
    return result

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))