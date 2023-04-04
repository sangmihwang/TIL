
def find_set(x):        # x가 속한 집합의 대표 리턴
    # rep[x] == x면 대표
    while x != rep[x]:      # x ==rep[x]가 될때까지
        x= rep[x]
    return x

def union(x, y):        # y의 대표원소가 x의 대표원소를 가리키도록
    rep[find_set(y)] = find_set(x)

# makeset()
rep = [i for i in range(6)]
print(rep)