import check
from my_package.math import tools as tool # 패키지간의 연결은 .으로 표시
# from my_package.math.tools import pi, my_max # tools모듈의 특정 함수나 변수 가져오기

# # tools모듈의 모든 값 가져오기 / 사용한 기능을 표시하기 위해 * 보단 정확히 명시하여 가져오도록 하자
# 또한 *로 불러올시 변수나 함수명이 동일하게 될 수 있으므로 주의!
# from my_package.math.tools import *

# print(dir(check)) # 어떤 메소드를 사용할 수 있는지 확인 리스트

# check_even = check.even
# print(check_even(0))

# print(tools.pi) # from math import tools
# print(pi) # from tools omport pi
# print(my_max(4, 5))

print(tool.e)