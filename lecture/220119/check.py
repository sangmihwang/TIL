# Tools로부터 뭔가 가죠와

from calc import tools

print(tools.add(1, 2))
print(tools.sub(3, 4))


from calc.tools import add, sub

print(add(1, 2))
print(sub(3, 4))

alias: 별칭을 지어준다
  -> 모듈의 함수이름이 너무 길거나, 겹칠 때 사용하는 기능

from calc.tools import sub as tools_sub, add_from_test_and_a_is_first_parameter as add
# 예를 들어 utils 모듈에도 sub 함수가 존재한다면 아래와 같이 가져옴
# calc 패키지의 utils 모듈에서 sub 함수를 가져오는데,
#       이 파일에서 해당 sub 함수를 utils_sub 라는 이름으로 부르겠다.
from calc.utils import sub as utils_sub

print(add(1, 2))

# sub 는 누구일까 ?
print(tools_sub(3, 4))
print(utils_sub(3, 4))