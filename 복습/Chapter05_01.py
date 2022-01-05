# Chapter05-1
# 파이썬 함수 및 중요성
""" 
함수의 장점 
1. 함수를 이용해 단계별 프로그래밍 가능
2. 각 개발자들이 함수에 집중해 함수와 함수 이외의 코드를 분리해 작성하기 때문에 코드의 안정성이 높아질 수 있다.
3. 함수를 모듈화해 사용하게 되면 코드의 재사용성을 막을 수 있다. 
""" 
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
      # code

# 예제1
def first_func(w1):
  print("Hello, ", w1)

word = "Goodboy"

first_func(word)

print()

# 예제2
def return_func(w1):
  value = "Hello, " + str(w1)
  return value

x = return_func('GoodBoy2')
print(x)

# 예제3 (다중 반환)

def func_mul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return y1, y2, y3

x, y, z = func_mul(10) # 이 때 각 리턴 값에 맞는 변수 없으면 예러(에외)발생 - unpacking 개념
print(x, y, z)

print()

# 튜플 리턴
def func_mul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return (y1, y2, y3)

p = func_mul(10)
print(type(p), p)

# 리스트 리턴
def func_mul2(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return [y1, y2, y3]

q = func_mul2(10)
print(type(q), q)

# 딕셔너리 리턴
def func_mul3(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return {'v1':y1, 'v2':y2, 'v3':y3}

d = func_mul3(10)
print(type(d), d, d.get('v2'), d.keys(), d.items())

# 중요
# *args - tuple로 인자들 packing, **kwargs - dict로 인자들 packing

# *args(함수 안에서 args로 사용 가능) - 중요한건 아스타(*) 1개 이름은 자유
def args_func(*args): # 매개변수 명 자유
  # enumerate -> return (인덱스번호, 요소) -> tuple 형태 ex) ((0, 'Lee'), (1, 'Park'))
  for i in enumerate(args):
    print('Result : {}'.format(i) )
  for i, v in enumerate(args):
    print('Result : {}'.format(i), v)
  print('----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')


# **kwargs(함수 안에서 kwargs로 사용가능) - 중요한건 아스타(**) 2개 이름은 자유
def kwargs_func(**kwargs):
  print(kwargs)
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v])
  print('----')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Cho')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
  print(args_1, args_2, args, kwargs)

example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1 = 20, age2 = 30, age3 = 40)

# 중첩함수

def nested_func(num):
  def func_in_func(num):
    print(num)
  print("In func")
  func_in_func(num * 100)

nested_func(100)

print()


# 실행불가
# func_in_func(1000) 함수 안에 함수가 메모리에 할당되는 경우는 해당 함수를 포함하는 상위 함수가 실행되어 정의 될 때 뿐이다. 상위의 함수의 실행 없이 내부 함수를 실행할 수 없다. 캡슐화 -> 실행 context 개념 떠올려서 생각

# 람다식 예제
# 람다식 장점 -> 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# 파이썬에서 일반적인 함수 선언
# def mul_func(x, y):
#   return x * y

# 파이썬에서 람다식 선언 -> 함수표현식으로 사용 또는 함수안에 인자를 함수로 줄 때 람다식으로 함수를 줄 수 있다. (이외에 함수를 인자로 줄려면 변수에 함수를 할당해서 줘야한다.)
# lambda x, y : x * y

# 일반적함수 -> 할당(함수 표현식), 함수 선언문 가능
def mul_func(x, y):
  return x * y

print(mul_func(10 ,50))

print()

mul_func_var = mul_func
print(mul_func_var(20, 50))

# 람다 함수 -> 할당(함수 표현식만 가능)
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50,50))

# js와 마찬가지로 이렇게 작성할 시 즉시실행함수가 된다. -> 강의에 없음 그냥 해본 것
print((lambda x, y: x * y)(20, 50))

def func_final(x, y, func):
  print('>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda_mul_func)

# Hint -> 인자 및 리턴값이 어떠한 타입일지 알려주는 용도
def tot_length1(word: str, num: int) -> int:
  return len(word) * num

print('hint exam1 : ', tot_length1("i love you",10))

# 실제 인자 타입과 힌트의 타입이 달라도 에러가 발생하지는 않는다.
def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)


tot_length2("niceman", 10)


































































