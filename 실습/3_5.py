number_of_people = 0
import book 

# 회원수를 늘리는 함수
def increase_user():
    global number_of_people
    number_of_people += 1
    

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 회원을 만드는 함수
def create_user(name, age, address):
    #회원 총원 + 1
    increase_user()

    #유저 정보를 딕셔너리로 만들기
    user_dict = {
        'name' : name,
        'age' : age, 
        'address' : address
    }
    print (f'{name}님 환영합니다!')
    return user_dict

# 유저 목록    
use_list = list(map(create_user, name, age, address))
print(use_list)

#address를 어떻게 제외? -> 무시해버리기
def make_new_user_list(user_info):
    result = {
        'name' : user_info['name'],
        'age' : user_info['age'] //10
    }
    return result

new_user_list = map(make_new_user_list, use_list) 
print(new_user_list)

# 렌탈이 진행되는 함수
def rental_book(use_info):
    # 남은 책 수 계산
    book.decrease_book(use_info['age'])
    print(f'{use_info["name"]}님이 {use_info["age"]}권을 대여 했습니다')


list(map(rental_book, new_user_list))  