# four squared(재귀...)
# import sys
#
# # 무조건 4개안에 답이 있음
# def four_squares(n):
#     # 어떤 자연수 하나의 제곱으로 가능한 경우
#     if int(n**0.5) == n**0.5:
#         return 1
#
#     # 2개의 자연수
#     for i in range(1, int(n**0.5)+1):
#         if int((n-i**2)**0.5) == (n-i**2)**0.5:
#             return 2
#
#     # 3개의 자연수
#     for i in range(1, int(n**0.5)+1):
#         for j in range(1, int((n-i**2)**0.5)+1):
#             if int((n-i**2-j**2)**0.5) == (n-i**2-j**2)**0.5:
#                 return 3
#
#     # 나머지는 4개
#     return 4
#
#
# N = int(sys.stdin.readline())
# print(four_squares(N))

# 동전게임
import sys
'''
H : 앞면
T : 뒷면
'''

# 행 뒤집기
def c_change(j):
    for i in range(3):
        if coins[i][j] == 'H':
            coins[i][j] = 'T'
        else:
            coins[i][j] = 'H'


# 열 뒤집기
def r_change(i):
    for j in range(3):
        if coins[i][j] == 'H':
            coins[i][j] = 'T'
        else:
            coins[i][j] = 'H'


# 왼쪽 대각선 뒤집기
def lc_change(i,j):
    for i in range(3):
        for j in range(3):
            if i == j:
                if coins[i][j] == 'H':
                    coins[i][j] = 'T'
                else:
                    coins[i][j] = 'H'


# 오른쪽 대각선 뒤집기
def rc_change(i, j):
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            if i == j:
                if coins[i][j] == 'H':
                    coins[i][j] = 'T'
                else:
                    coins[i][j] = 'H'


T = int(sys.stdin.readline())

for test_case in range(T):
    coins = [list(sys.stdin.readline().split()) for _ in range(3)]

    


