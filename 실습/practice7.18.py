# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)
print(5 / 3)

# 지수 표현
print(314e-2)
print(314e2)

# f-string
bugs = 'roaches'
counts = 100
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')
print('Debugging {} {} {}'.format(bugs, counts, area))
print('Debugging %s %d %s' % (bugs, counts, area))

# f-string 응용
greeting = 'hi'
print(f'{greeting:^10}') # 10칸 부여, 가운데 저장
print(f'{greeting:>10}') # 10칸 부여, 가운데 저장
print(f'{3.141592:.4f}') # 4자리수까지

# 불변과 가변
my_str = 'hello'
# my_str[0] : 'z'

my_list = [1, 2, 3]
my_list[0] =100
print(my_list)

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1)
print(list_2)

x = 10
y = x

x = 20
print(x)
print(y)


