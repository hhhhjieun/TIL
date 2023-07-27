number_of_people = 0

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
    
result = list(map(create_user, name, age, address))

print(result)