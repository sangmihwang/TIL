# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = ''
    for i in range(len(word)):
        for alphabet in word:
            # 소문자인 경우
            if alphabet.islower() == True: 
                num_old = ord(word[i])
                if num_old + n > 122:
                    num_new = num_old + n - 122 + 96
                else:
                    num_new = num_old + n
                
            # 대문자인 경우
            else:
                num_old = ord(word[i])
                if num_old + n > 90:
                    num_new = num_old + n - 90 + 64
                else: 
                    num_new = num_old + n
        result = result + chr(num_new)   # 문자열 그대로 가져와야하는 경우 '+' 사용
    return result



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
