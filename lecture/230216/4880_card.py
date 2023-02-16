def f(i, j):
    if i == j:
        return i
    else:
        m = (i+j) // 2
        m1 = f(i, m)
        m2 = f(m+1, j)
        return win(m1, m2)

def win(a, b):
    if (card[a], card[b]) in [(1,3),(2,1),(3,2)]:
        return a
    elif (card[a], card[b]) in [(3,1),(1,2),(2,3)]:
        return b
    else:
        return a

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))

    print(f'#{t} {f(0, N-1) + 1}')



