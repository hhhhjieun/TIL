# num = int(input("숫자를 입력하세요 : "))

# # if statement
# # num이 홀수라면 (2로 나눈 나머지가 1이라면)
# if num % 2 == 1:
# # if num % 2: # 이것도 작동은 함(결과값인 1이 True로 반환, 0은 False)
#     print('홀수입니다.')
# # num이 홀수가 아니라면(짝수)
# else:
#     print('짝수입니다.')
    

# 중첩된 반복문
# outers = ['A', 'B']
# inners = ['C', 'D']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)

# List Comprehension
# 홀수만 있는 리스트 만들기 (0~9)
# 1. 일반적 방법
# new_list = [ ]
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list)

# # 2. list comprehension
# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)

# 리스트를 생성하는 3가지 방법
# 정수 1,2,3을 가지는 새로운 리스트 만들기
# 어떤게 제일 빠른가

# numbers = ['1', '2', '3']

# # 1. for loop
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers) # [1, 2, 3]

# # 2. map
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2) # [1, 2, 3]

# # 3. list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3) # [1, 2, 3]

# enumerate 예시
# result = ['a', 'b', 'c']

# print(enumerate(result))
# print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]

# for index, elem in enumerate(result): #enumerate의 값이 튜플 > 변수 2개
#     print(index, elem) # 0 a  1 b  2 c

import requests
from pprint import pprint as print

# 빈 리스트 생성
dummy_data = []


for i in range(1,2):
    # 경로에 숫자 붙이기
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    # print(API_URL)
    response = requests.get(API_URL)
    parsed_data = response.json()
    #print(parsed_data)
    
    dict_company = dict(parsed_data['company'])
    dict_address = dict(parsed_data['address'])
    dict_geo = dict(dict_address['geo'])
    
    dummy_dict = {'name' : parsed_data['name'], 'lat' : dict_geo['lat'], 
                  'lng' : dict_geo['lng'], 'company name' : dict_company['name'] }
    print(dummy_dict)
    
    dummy_data.append(dummy_dict)

    print(dummy_data)
    
    # dummy_data에 name 넣기
    # dummy_data.append(parsed_data['name'])
    # print(parsed_data['name'])



# print(dummy_data)

# print(parsed_data)
