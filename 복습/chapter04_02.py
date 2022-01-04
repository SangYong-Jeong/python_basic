# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for i in <collection>
#   <loop body>

# range
# 인자 하나만 선언시 0 ~ 인자 - 1까지의 리스트임
# 인자 여러개 선언시 statr, stop, step으로 구분
# state ~ stop - 1 까지의 리스트 (이를 step으로 가져옴)
# step이 음수 이면 start가 stop보다 커야함
for v1 in range(10): 
  print("v1 is : ", v1)

print()

for v2 in range(1, 11):
  print('v2 is : ', v2)

print()

for v3 in range(1, 11 ,2):
  print("v3 is :", v3)

print()

# 1 ~ 1000합

sum1 = 0

for v in range(1, 1001):
  sum1 += v

print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001))) # sum(리스트)
print('1 ~ 1000 안에 4의 배수의 합', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 속성 갖고 있는 것 리턴해주는 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
  print("You are", name)

print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
  print("Current number : ", number)

print()

# 예제3
word = 'Beautiful'

for s in word:
  print('word : ', s)

# 예제4
my_info = {
  "name": "Lee",
  "Age": 33,
  "City": "Seoul"
}

for key in my_info:
  print(key, ":", my_info[key])

for val in my_info.values():
  print(val)

print()

# 예제5
name = 'FineApplE'

for n in name:
  if n.isupper():
    print(n)
  else:
    print(n.upper())

print()

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
  if num == 34:
    print("Found : 34!")
    break
  else:
    print("Not found : ", num)

print()

# continue -> continue 만나면 continue 아래 구문 실행 x 다음 요소로 넘어간다.
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
  if type(v) is bool: # is 연산자는 타입 비교 할 때 쓰이는 연산자이다.
    continue
  
  print("current type : ", type(v))
  print("multiply by 2:", v * 3)

# else 구문 -> for문을 전부 끝낸 후 실행 되는 구문 -> 중간에 break로 빠져 나가면 실행되지 않는다.
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
  if num == 34: # 45
    print("Found : 34!")
    break
else:
  print("Not Found 45...")

# 구구단 출력

for i in range(2, 10): # 2 ~ 9
  for j in range(1, 10): # 2 ~ 9
    print('{:4d}'.format(i * j), end='')
  print()

# 변환 예제
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name))) # 순서 x



















































