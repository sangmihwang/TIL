# 끝말잇기 -> 몇 번째 사람이 탈락하는 지 확인하는 코드를 작성하시오.
words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# 과거에 입력된 단어들
before_words = []

# 앞서 입력된 단어의 마지막 문자로 시작하는 단어를 말해야 한다.
while True:
    word = input('단어 입력: ')

    # 만약 첫 번째 단어라면
    if len(before_words) == 0:
        before_words.append(word)
        continue

    # 끝말잇기를 틀리거나 이전에 등장했던 단어를 사용하는 경우 진다.
    # if before_words[-1][-1] == word[0] and (word not in before_words):
    if before_words[-1][-1] != word[0] or (word in before_words):
        print(f'{len(before_words) + 1}번째 사람이 틀렸다.')
        break
    else:
        print('정상이다')
        before_words.append(word