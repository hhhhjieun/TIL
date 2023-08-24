# 1063 킹
'''

R : 한 칸 오른쪽으로(0)
L : 한 칸 왼쪽으로(1)
B : 한 칸 아래로(2) -> y값이 -1
T : 한 칸 위로(3) -> y값이 +1
RT : 오른쪽 위 대각선으로(4)
LT : 왼쪽 위 대각선으로(5)
RB : 오른쪽 아래 대각선으로(6)
LB : 왼쪽 아래 대각선으로(7)

'''

import sys

# 위치 이동 함수
def location(king_location, stone_location, k):

    nx_k = king_location[0] + move_x[k]
    ny_k = king_location[1] + move_y[k]


    if nx_k == stone_location[0] and ny_k == stone_location[1]:
        nx_s = stone_location[0] + move_x[k]
        ny_s = stone_location[1] + move_y[k]
        if 0 < nx_k < 9 and 0 < ny_k < 9 and 0 < nx_s < 9 and 0 < ny_s < 9:
            king_location = [nx_k, ny_k]
            stone_location = [nx_s, ny_s]

    else:
        if 0 < nx_k < 9 and 0 < ny_k < 9:
            king_location = [nx_k, ny_k]

    return king_location, stone_location


King, Stone, N = sys.stdin.readline().split()
king = list(King)
stone = list(Stone)

# 킹 위치 = [x, y]
x_k = ord(king[0]) - 64
y_k = int(king[1])
king_location = [x_k, y_k]

# 돌 위치 = [x , y]
x_s = ord(stone[0]) - 64
y_s = int(stone[1])
stone_location = [x_s, y_s]


#         R, L, B,  T, RT, LT, RB, LB
move_y = [0, 0, -1, 1, 1, 1, -1, -1]
move_x = [1, -1, 0, 0, 1, -1, 1, -1]

for _ in range(int(N)):
    order = sys.stdin.readline().strip()  # 명령

    if order == 'R':
        k = 0
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'L':
        k = 1
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'B':
        k = 2
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'T':
        k = 3
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'RT':
        k = 4
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'LT':
        k = 5
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'RB':
        k = 6
        king_location, stone_location = location(king_location, stone_location, k)

    elif order == 'LB':
        k = 7
        king_location, stone_location = location(king_location, stone_location, k)


# 마지막 킹 위치 = [x, y]
final_x_k = chr(king_location[0] + 64)
final_y_k = str(king_location[1])
king_location = [final_x_k, final_y_k]
king_result = ''.join(king_location)

# 돌 위치 = [x , y]
final_x_s = chr(stone_location[0] + 64)
final_y_s = str(stone_location[1])
stone_location = [final_x_s, final_y_s]
stone_result = ''.join(stone_location)

print(king_result)
print(stone_result)

