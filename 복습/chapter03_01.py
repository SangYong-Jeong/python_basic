# Chapter03-01
# 숫자형

# 파이썬 지원 자료형 
"""
int : 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 7
list = [str1, str2]
dict = {
  "name": "Machine Learning",
  "version": 2.0
}
tuple = (7,8,9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
'//' : 몫
%: 나머지
abs(x) 절대값
pow(x,y) == x ** y
"""

# 정수 선언
i = 77
i2 = -14
big_int = 182312893718

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141
f3 = -3.9
f4 = 3/9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습 -> 눈으로
# 서로다른 형(type)을 계산하면 형 변환이 자동으로 이루어진다.

a = 3. # 3.0 (0생략가능)
b = 6
c = .7 # 0.7 (0생략가능)
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 수치 연산 함수
print(abs(-7))

x, y = divmod(100, 8) # return 몫, 나머지
print(x, y)
print(pow(2, 3), 2 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)