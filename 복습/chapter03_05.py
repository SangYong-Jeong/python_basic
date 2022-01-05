# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birt': '870124'}
b = {0: 'Hello python!'} # 키값은 문자열이 아니어도 가능
c = {'arr': [1,2,3,4]} # 요소에도 어떤 타입이든 가능
d = { # 펼쳐서 선언 가능
  'Name': 'Niceman',
  'City': 'Seoul',
  'Age': '33',
  'Grade': 'A',
  'Status': True
}
e = dict([ # 이렇게 dict(리스트[tuple()]) 형태로 dict 자료형 선언 가능
  ('Name', 'Niceman'),
  ('City', 'Seoul'),
  ('Age', '33'),
  ('Grade', 'A'),
  ('Status', True)
])

f = dict( # 이렇게도 선언가능! 이럴경우 -> key값은 str
  Name='Niceman',
  City='Seoul',
  Age='33',
  Grade='A',
  Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 존재X -> 에러발생
print('a - ', a.get('name')) # 존재 x -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(d))

# dict_keys, dict_vlaues, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

# list 형 변환
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

# list 형 변환
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

# list 형 변환 -> (key,value) -> list 형 변환 시 요소들이 tuple 형태
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

# dict형에서 pop은 key값을 꼭 넣어줘어야 한다. (because of 순서 x)
print('a - ', a.pop('name'))
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('d - ', d.pop('City'))

# python 3.8 이상 부터는 dict의 맨 뒤 값 부터 value값을 뽑아온다. 다 뽑은 상태에서 popitem() 시 에러 발생 (3.8ver 이전에는 random으로 추출)
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
# 예외(에러)
# print('f - ', f.popitem())

# in 연산자 - 해당 key가 a dict 안에 있는 지 물어보는 연산자
print('a - ', 'phone' in a)
print('a - ', 'addr' in a)

# 수정
print('f - ', f)
f.update(Age=36)

temp = {'Age': 27}

print('f - ', f)

f.update(temp)
f.update({'Age': 27})
print('f - ', f)

# 모두 제거
f.clear()
print('f - ', f)