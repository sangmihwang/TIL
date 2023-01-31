# import time
# st=time.time()


n = int(input())
lis=[]
for i in range(0, n+1):
    if i == 0 or i == 1:
        lis.append(int(i))    
    else:
        lis.append(lis[i-2] + lis[i-1])
        

print(lis[-1])
# print(fibo(n))
# print(f'Execution time:{time.time()-st} s')



