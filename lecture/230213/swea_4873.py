T = int(input())
for t in range(1, T+1):
    word = input()
    N = len(word)
    i = 0
    while 1 < N:
        if word[i] == word[i+1]:
            word = word[:i] + word[i+2:]
            N -= 2
            i = 0
        elif word[i] != word[i+1]:
            i += 1
        if i == N-1:
            break
    ans = len(word)

    print(f'#{t} {ans}')