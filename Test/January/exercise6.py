def de_identify(num):
    return str(num)[:6] + '*******'


print(de_identify('970103-1234567'))


grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
max = 0
for idx in grain_lst:   
    if idx[1] > max:
        max = idx[1]
    else:
        pass
# print(max)
    if idx[1] == max:
        ans = idx[0]
print(ans)


def count_vowels(word):
    count = 0
    for char in word:
        if char == 'a' or char =='e' or char =='i' or char =='o' or char == 'u':
            # char == 'a' or 'e' or 'i' or 'o' or 'u' 랑 뭐가 다른지
            count += 1
    return count

print(count_vowels('apple'))

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

entry_rank = Counter(entry_record)
exit_rank = Counter(exit_record)

print('입장 기록 많은 Top3')
for i in range(3):
    lst = entry_rank.most_common(3)
    print(lst[i][0], lst[i][1],'회')


diff_1 = entry_rank - exit_rank
diff_2 = exit_rank - entry_rank


for key in diff_1.keys():
    for value in diff_1.values():
        print(key,'은 입장 기록이', value,'회 더 많아 수상합니다.')
for key in diff_2.keys():
    for value in diff_2.values():
        print(key,'은 입장 기록이', value,'회 더 많아 수상합니다.')




