# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언 
n = 700

# 출력
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# id(identity)확인: 객체의 고유값 확인
# 객체의 여러 개가 같은 값으로 생성이 될 때는 하나의 객체만 생성되어 공유하고 있다.

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates (추천)

# 허용하는 변수 선언 법(특수문자는 _, $만 가능)
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 7

# 예약어는 변수명으로 불가능
## 자료 참고





