# 모듈 사용 실습

import sys

print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:/math')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))

import chapter06_02

print(__name__) # __main__ 일 경우 실행되는 그 파일 대상을 의미
print(chapter06_02.__name__)