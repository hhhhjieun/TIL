'''
# 기념품
import sys

N = int(sys.stdin.readline())  # 캠프 참가자수

# 참가자
players = [int(i) for i in range(1, N+1)]

# 참가자가 1명 남을때 까지
T = 1  # 단계
front = 0

while len(players) != 1:

    front = (front + (T**3) - 1) % len(players)
    players.pop(front)
    T += 1

print(players[0])
'''

# 주차장
'''
양의 정수 i : 차량 i가 주차장에 들어오는 것 의미
음의 정수 i : 차량 i가 주차장에서 나가는 것 의미
'''

import sys

N, M = map(int, sys.stdin.readline().split())  # N: 주차 공간의 수, M : 차량의 수

charges = list(int(sys.stdin.readline()) for _ in range(N))  # 주차 공간의 단위 무게당 요금

car = list(int(sys.stdin.readline()) for _ in range(M))  # 차량의 무게
cars = [[idx+1, weigh] for idx, weigh in enumerate(car)]  # 차량의 번호, 무게

total_income = 0  # 총 수입
parking_lot = [[0, 0] * N]  # 주차장 q
front = 0
rear = 0

# 주차
for i in range(2*M):
    car_num = int(input())
    # 입차
    if car_num > 0:
        if rear < N:
            parking_lot[rear] = cars[car_num-1]
            rear += 1


    # 출차
    else:
        pass









