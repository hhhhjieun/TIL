#import json # 내장 모듈

# # json 데이터
# json_data = '''
# {
#     "name" : "김싸피",
#     "age" : 28,
#     "hobbies" : [
#         "공부하기",
#         "복습하기"
#     ]

# }
# '''

# # 문자열에서 dict로 json.loads를 통해 변환
# data = json.loads(json_data)

# # data = dict(json_data) ???


# #json 데이터에서 원하는 데이터만 가져오기
# name = data.get('name')

# print(name)

API_KEY = 'f394f1bfa523217c0461db711decd436'
# 서울의 위도 경도를 활용해서 데이터를 받아왔다

# lat = 37.56
# lon = 126.97
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

city_name = 'Seoul,KR'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

# API 요청보내기
import requests
response = requests.get(url).json()
#print(response) 

# 온도만 출력
temp = response['main']['temp']
# 섭씨 온ㄷ 
temp -= 273.15
print(temp)


