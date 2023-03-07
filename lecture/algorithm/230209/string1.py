s = 'strings'
print(s[::-1])          # 뒤집기
                        # sgnirts

print(list(s))          # ['s', 't', 'r', 'i', 'n', 'g', 's']

s = list(s)
s.reverse()
print(s)                # ['s', 'g', 'n', 'i', 'r', 't', 's']

s = ''.join(s)
print(s)                # sgnirts