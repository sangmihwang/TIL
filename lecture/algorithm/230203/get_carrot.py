# def sum(list):
#     sum = 0
#     for n in list:
#         sum = sum + n
#     return sum



T = int(input())
for t in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))
    sum_min = 20
    
    for i in range(len(carrot)):
        
        d = abs(sum(carrot[:i]) - sum(carrot[i:]))
        if d < sum_min:
            sum_min = d
            ans = i
        
    print(f'#{t+1} {ans} {sum_min}')
    
