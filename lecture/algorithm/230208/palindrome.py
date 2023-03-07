T =  int(input())
for t in range(1, T+1):
    word = input()
    ans = 0
    for i in range(len(word)):
        if word[i] == word[len(word)-1 -i]:
            ans = 1
        else: break
    print(f'#{t} {ans}')