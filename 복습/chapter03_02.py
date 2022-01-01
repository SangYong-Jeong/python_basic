# Chapter 03-2
# 파이썬 문자형(중요!)

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4= '''Thank you!'''

print (type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 공백포함 길이

# 빈 문자열
str1_t1 = '' # or ""
str2_t2 = str()

print(str1_t1, type(str1_t1), len(str1_t1))
print(str2_t2, type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용 -> 원래 사용 되는 방식 탈출(이스케이프)
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자 \ 문자 표시
\' : 문자 ' 문자 표시
\" : 문자 " 문자 표시
\000 : 널 문자
...

"""
# I'm Boy

print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = "What\'s on TV?"
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 출력 -> escape를 사용하지 않는 방법(escape 무시)
raw_S = r'D:\python\test'

print(raw_S)

# 멀티라인 출력
multi_str1 = \
"""
문자열 
멀티라인 입력
테스트
"""
print(multi_str1)

# 멀티라인(역슬래시) 출력
multi_str2 = \
'''
문자열 멀티라인
역슬래시(\) \
테스트
'''
print(multi_str2)

# 문자열 연산
str_o1 = 'Python'
str_o2 = 'Apple'
str_o3 = 'How are you doing?'
str_o4 = 'Seoul Daejeon Busan Jinju'

print(3 * str_o1) # 문자열 * int형 -> 문자열 int형 값 만큼 반복
print(str_o1 + str_o2) # 문자열 + 문자열 -> str
print(dir(str_o1)) # __iter__ (반복 가능 속성)
print('y' in str_o1) # y가 str_o1에 있니? return bool
print('n' in str_o1) 
print('P' not in str_o2)

# 문자열 형 변환
print(type(str(66))) # type int -> str
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print(str(complex(12)), type(str(complex(12))))

# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha 등 ...)
print("Capitalize: ", str_o1.capitalize()) # 첫 문자 대문자로
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm", "!"]))
print("replace1: ", str_o1.replace("are", "was"))
print("replace2: ", str_o3.replace("are", "was"))
print("split: ", str_o4.split(' '))
print("sorted: ", sorted(str_o1))
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# 반복 (시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 확인

# 출력
for i in im_str:
  print(i)

# 슬라이싱
str_sl = 'Nice Python'

# 슬라이싱 연습
print(str_sl[0:3]) # 뒤에 숫자 -1 까지 
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-4:-2])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])

# 아스키코드
a = 'z'

print(ord(a))
print(chr(122))

