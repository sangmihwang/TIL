N = int(input())
sum = 0
lst = []
for n in range(1, N+1):
    num_lst = list(map(int, str(a)))
    sum = n + sum(num_lst)
    if sum == N:
        lst.append(a)
if len(lst) == 0:
    print(0)
else:
    print(min(lst))

