# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x)

# 선언
a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print()

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
# 형 변환
print('e - ', list(e[-1][1]))
print('e - ', list(e[-1]))

# 수정 x
# d[0] = 1500 -> error 발생

# 슬라이싱 -> return tuple(해당 인덱스 요소를 포함한)
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>')
print('c + d - ', c + d)
print('c * 3', c * 3)
# print("c[0] + 'hi' - ", c[0] + "hi")
print("Test + c[0] - ", "Test" + str(c[0]))

# 팩킹 & 언팩킹(Packing, and Unpacking) -> 언팩킹은 js의 구조분해할당 문법으로 이해

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t)
print(t[0])
print(t[-1])
print()

# 언팩킹1 -> () 없어도 가능 -> 해당 튜플의 요소만큼 변수 선언해 언팩킹 해야 한다! 
(x1, x2, x3, x4) = t

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = 4
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

""" 
tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없다.
list와 마찬가지로 요소에는 다양한 타입이 함께 포함될 수 있다.
"""
