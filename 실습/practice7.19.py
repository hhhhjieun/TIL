# 함수
# def greet(name):  # name은 매개변수(parameter) 
#     message = 'Hello, ' + name
#     return message

# name_1 = input() 
# result = greet(name_1) # name_1 인자(argument)
# print(result)

# 위치인자
# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')

# greet('Alice', 25)

#임의의 인자 목록
# def calculate_sum(*args):
#     print(args)
#     total = sum(args)
#     print(f'합계 : {total}')

# result = map(int, input().split())
# calculate_sum(*result) # 리스트 언패킹

# 임의의 키워드 인자 목록
def print_info(**kwargs):
    print(kwargs) 
    
   
print_info(name = input(), age = int(input()))
# print_info(name = 'Eve', age = 30)





# 모듈 
# import my_package.math.my_math as my_math

# print(my_math.pi)

# print(my_math.add(100, 200))

# import requests 

# url = 'https:\/\/images.dog.ceo\/breeds\/pembroke\/n02113023_6312.jpg'
# response = requests.get(url).json()

# print(response)

