# f'문자열 {변수} 문자열'

name = 'Kim', "Park"
score = 50, 60

print(f'이름: {name}, 점수: {score}')

month = 1
while month <= 12:
    print(f'2020년 {month}월')
    month = month + 1

# abc에 따옴표 안 해서 계속 오류
nums = ['a', 'b', 'c', 'd', 'e']
for i in nums:
    print(f'{i}조')

# 그냥 n번 반복 실행
for i in range(5): 
    print('a')

