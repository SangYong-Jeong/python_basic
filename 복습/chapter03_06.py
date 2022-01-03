# Chapter03-6
# 집합(Sets) 특징
# 집합(Sets) 자료형(순서x, 중복x)

# 선언
a = set() # {} 로 선언하는건 dict형
b = set([1, 2, 3, 4])
c = set([1, 4, 5 , 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1,2,3,), 3.14159}

print('a - ', type(a) , a)
print('b - ', type(b) , b)
print('c - ', type(c) , c)
print('d - ', type(d) , d)
print('e - ', type(e) , e) # 중복x 때문에 'foo' 는 한 번만 찍힌다.
print('f - ', type(f) , f)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e)) # 중복 제거되서 요소는 4개

# 집합 자료형 활용 - > set type 끼리만 가능한 연산
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
print('l - ', s1 & s2) 
print('l - ', s1.intersection(s2))

# 합집합
print('l - ', s1 | s2)
print('l - ', s1.union(s2))

# 차집합(교집합 부분 빼고 남은 부분)
print('l - ', s1 - s2)
print('l - ', s1.difference(s2))

# 중복 원소 확인 (dis -> 반대 개념) -> 교집합 있으면 False, 없으면 True
print('l - ', s1.isdisjoint(s2))

# 부분 집합 확인 
print('l - ', s1.issubset(s2)) # s1이 s2의 부분집합인가?
print('l - ', s1.issuperset(s2)) # s2가 s1의 부분집합인가?

# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7) # 해당 원소가 없으면 에러가 난다.

s1.discard(3) 
print('s1 - ', s1)
# s1.discard(7) # 해당 원소가 없어도 에러가 나지 않는다.

# 모두 제거
s1.clear()
print('s1 - ', s1)

