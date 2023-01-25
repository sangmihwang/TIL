

# num 번째 자리의 피보나치 수 구하기
def fibo(n):
    # 종료 조건
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    # 다음으로 넘어감
    # 최종적으로 우리가 return 받고자 하는 값을 생각하면 작성하기 쉽다
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(12))