# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = '' # or ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용 -> 예제파일에 여러가지 있음 확인 필요
# I'm Boy

print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력 -> escape를 사용하지 않는 방법(escape 무시) 
raw_s = r"D:\python\test"

print(raw_s)

# 멀티라인 입력
# 역슬래시 사용 (문자열 표현 방식에서 줄바꿈을 막는 역할)
multi_str = \
"""
문자열 
멀티라인 입력  
테스트
"""

print(multi_str)


# 문자열 연산
str_o1 = 'Python'
str_o2 = 'Apple'
str_o3 = 'How are you doing'
str_o4 = 'Seoul Daejeon Busan Jinju'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # y라는 알파벳이 포함되어있니? (시퀀스형이 쓸 수 있음) 
print('z' in str_o1) 
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
# 추가적인 부분 예제 파일 확인
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("!"))
print("replace", str_o1.replace("thon", " Good"))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 가 있으면 반복 가능

# 출력
for i in im_str:
  print(i)


# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2 인덱스의 str 이 합쳐져서 나온다.
print(str_s1[5:]) # [5:11] 같다(5부터 끝까지 가져와)
print(str_s1[:len(str_s1)]) # str_sl[:11] (첫부분도 생략가능 0임)
print(str_s1[:len(str_s1) - 1]) # str_sl[:10] (첫부분도 생략가능 0임)
print(str_s1[:]) # str_sl[:11]
print(str_s1[1:9:2]) # 2칸 씩 뛰어서 가져와라
print(str_s1[-5:])
print(str_s1[1: -2])
print(str_s1[::2]) # 처음 부터 끝까지 2칸 간격으로 가져와라
print(str_s1[::-1]) # 음수는 오른쪽에서 왼쪽으로

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로
