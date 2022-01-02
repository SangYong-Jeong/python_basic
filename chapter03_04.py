# Chapter 03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언
a = ()
# 괄호가 없어도 튜플 선언 가능
b = (1,) # 원소가 하나일때는 끝에 ,를 써줘야 tuple 자료형이된다. 2개일 때 부터는 상관 없다.
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1]))

# 수정x
# d[0] = 1500

# 슬라이싱
print('>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산 - 내부에 원소가 변경되거나 삭제되지 않는다면 연산을 통한 튜플의 원소의 개수가 늘어나는 것은 허용
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 괄호가 없어도 언패킹 된다. 하지만 가독성 측면에서 언패킹 했다고 괄호를 쳐서 표시 해주는게 좋다.
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3 ,x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 괄호가 없어도 튜플
t3 = 4, # 튜플
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6 # 언패킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)




















