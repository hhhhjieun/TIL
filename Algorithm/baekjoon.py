# 세로 읽기
# 총 다섯줄의 입력
# arr = [list(map(str, input())) for _ in range(5)]
#
#
# # 열의 최댓값 찾기
# max_length = 0
# for i in range(5):
#     length = len(arr[i])
#     if max_length < length:
#         max_length = length
#
# # max_length 를 기준으로 빈 행렬 만들기
# new_arr = [[0] * max_length for _ in range(5)]
#
# # 새로운 행렬에 기존 행렬 입력
# for i in range(5):
#     for j in range(len(arr[i])):
#         new_arr[i][j] = arr[i][j]
#
#
# # 2차원 배열로 열 우선
# for j in range(max_length):
#     for i in range(5):
#         if new_arr[i][j] == 0:
#             continue
#         else:
#             print(new_arr[i][j], end='')


# 색종이
# 색종이 수
T = int(input())
canvas = [[0] * 100 for _ in range(100)]

for num in range(T):
    R = 10  # 변의 길이
    width_start, height_start = map(int, input().split())

    width_end = width_start + R
    height_end = height_start + R

    for i in range(height_start, height_end):
        for j in range(width_start, width_end):
            canvas[i][j] += 1

# 넓이 계산하기
# 값이 1 이상인 경우 계산
area = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] >= 1:
            area += 1

print(area)

