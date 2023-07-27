black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

import requests
#from pprint import pprint as print

# 빈 리스트 생성
dummy_data = []


for i in range(1,11):
    # 경로에 숫자 붙이기
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    # print(API_URL)
    response = requests.get(API_URL)
    parsed_data = response.json()
    # print(parsed_data)
    
    #company_name, lat, lng 뽑기
    dict_company = dict(parsed_data['company'])
    dict_address = dict(parsed_data['address'])
    dict_geo = dict(dict_address['geo'])

    #dummy_dict 생성하기
    dummy_dict = {'name' : parsed_data['name'], 'lat' : dict_geo['lat'], 
                  'lng' : dict_geo['lng'], 'company name' : dict_company['name'] }

    # 조건문
    if -80 < float( dict_geo['lat']) < 80 and -80 < float(dict_geo['lng']) < 80:
        dummy_data.append(dummy_dict)

#create_user 함수 정의 
def create_user(company, user):
    users = []
    users.append(user)
    # 값을 딕셔너리로 생성
    censored_user_list = {company : users}
    #print(censored_user_list)
    return censored_user_list

# 넘겨받은 리스트로 인자 생성
for num in range(0,6):
    #dummy_data list 안에 있는 딕셔너리로 존재 > 딕셔너리의 값을 리스트로 변환
    li_data = list(dummy_data[num].values())
    #함수 호출
    li_user = create_user(li_data[3], li_data[0])
        #print(li_user)

    def censorship(company,user):
        user = ''.join(user_1)
        if str(company) in black_list:
            print(f'{company}소속의{user}은/는 등록할 수 없습니다.')
            return False
        else:
            print(f'이상 없습니다')
            return True
    
    #print(list(li_user.keys()))

    #list를 문자형으로 변환
    company_1 = ''.join(list(li_user.keys()))
    user_1 = li_user
    
    #censorship 함수 호출 및 return 값
    result = censorship(company_1, user_1)
    #print(result)


    if result is True:
        censored_user_list = {}
        censored_user_list[company_1] = user_1
    

print(censored_user_list)