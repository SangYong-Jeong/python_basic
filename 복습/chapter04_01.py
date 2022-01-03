# Chapter04-1
# 파이썬 제어문
# IF 실습

# 기본 형식

print(type(True)) # 0이 아닌 수, "abc", [1,2,3...], (1,2,3,...) ..
print(type(False)) # 0, "", [], (), {}

# 예1
if True:
  print("Good") # 파이썬에서는 조건에 맞을시 실행하는 부분을 들여쓰기로 표현 들여쓰기 중요 (Indent) 

if False:
  # 실행 x
  print("Bad")

# 예2
if False:
  # 여기는 실행되지 않음.
  print("Bad")
else:
  # 여기가 실행된다.
  print("Good")

# 관계연산자 종류
# >, >=, <, <=, ==, !=

x = 15
y = 10

# == 양 변이 같을 때 참.
print(x == y)

# != 양 변이 다를 때 참
print(x != y)

# > 왼쪽이 클 때 참
print(x > y)

# >= 왼쪽이 크거나 같을 때 참
print(x >= y)

# < 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

# 참 거짓 판별 종류
# 참: "values", [values], (values), {values},
# 거짓 : "", [], {}, 0, None

city = ""
if city:
  print("You ar in", city)
else:
  # 출력
  print("Please enter your city")

city = "Seoul"
if city:
  print("You are in:", city)
else:
  # 출력
  print("Please enter your city")