N = int(input())
lst = []
sum = 0
for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    for f in range(9):
                        sum += (100000*a + 10000*b + 1000*c + 100*d + 10*e + f) + (a+b+c+d+e+f)
                        if sum == N:
                            lst.append(100000*a + 10000*b + 1000*c + 100*d + 10*e + f)
                        sum = 0
print(min(lst))