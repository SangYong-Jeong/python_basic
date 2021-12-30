# Chapter02-1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Pythond Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")
print()

# separator 옵션
print('P','Y','T','H','O','N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')
print()

# end
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
# 특정 파일에 문자열 입력시 사용
print()

# format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))
print('{:<10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))
print('{:>10.5}'.format('pythonstudy'))

print()

# %d 
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42)) 
# expression 에서 s 제외하고는 d 나 f를 붙인다. (자릿수 조정시)

print()

# %f
print('%f' % (3.141592653588783))
print('{}'.format(3.141592653588783)) 
# :f 를 안 붙이면 전부 다 출력
print('{:f}'.format(3.141592653588783))

print('%06.2f' % (3.141592653588783))
# 정수부는 총 자릿수 (소수점 포함) 소수부는 소수점이하 자릿수 의미 정수부 앞에 0은 빈 공간에 0을 채운다는 의미
print('{:06.2f}'.format(3.141592653588783))
