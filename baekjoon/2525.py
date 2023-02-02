hour, min = map(int,input().split())
oven_time = int(input())
min = min + oven_time

for i in range(1, 170):
    
    if min // 60 == i:
        hour += i
        min = min % 60
    
if hour >= 24: 
    hour= hour - 24

print(hour, min)


for i in range(5):
             print(i)

