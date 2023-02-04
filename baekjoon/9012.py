T = int(input())
for t in range(T):
    VPS = str(input())
    cnt = 0

    for v in VPS:
        if v == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:         # cnt가 음수가 되는 순간
            break           # VPS 는 성립 안한다는것 간과
            
    if cnt == 0:
        print("YES")
    else:
        print("NO")
    