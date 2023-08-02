# 행열 탐색 연습

# 0으로 초기화 된 N * M 의 2 차원 배열 생성하기
from pprint import pprint as pp

# m = 5
# n = 5
#
# arr = []
# for i in range(n):
#     row = [0] * m
#     arr.append(row)

# pp(arr)

# 1. 행 우선 순회를 다른 것보다 우선시 하여 학습
num_list = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

for r in range(len(num_list)):
    for c in range(len(num_list)):
        pass
        # print(f'{num_list[r][c]}', end =' ')  # 1 2 3 4 5 6 7 8 9

# 2. 열 우선 순회
for c in range(len(num_list)):
    for r in range(len(num_list)):
        pass
        # print(f'{num_list[r][c]}', end=' ') # 1 4 7 2 5 8 3 6 9

# 3. 역-행 우선 순회
for i in range(len(num_list)):
    for j in range(len(num_list)-1, -1, -1):
        pass
        # print(num_list[i][j], end = ' ')  # 3 2 1 6 5 4 9 8 7

# 4. 역-열 우선 순회
for i in range(len(num_list)-1, -1, -1):
    for j in range(len(num_list)):
        pass
        # print(num_list[j][i], end=' ')  # 3 6 9 2 5 8 1 4 7

# 5. 가장자리 합

def edge_sum(arr):
    # 순회를 하면서, 2차원 리스트의 가장자리에 있는 원소들을 합한다
    edge_sum_result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr) - 1:
                print(arr[i][j], end=' ')  # 1 2 3 4 6 7 8 9
                edge_sum_result += arr[i][j]

    return edge_sum_result


result = edge_sum(num_list)
print(result)  # 40

# 델타 검색
# 문제에 제시된 제약 조건에 따라 탐색 순서는 달라질 수 있다
# 대각선
# 하 우 좌 상 (순서가 바뀔 수 잇음)
# 리스트로 설정 > 키 값 확인

        # 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]

# 튜플로

# 대각선
     #   좌상단    좌하단    우하단   우상단
dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

for nx, ny in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    pass

def without_delta():
    print(num_list[r - 1][c])  # 상
    print(num_list[r + 1][c])  # 하
    print(num_list[r][c - 1])  # 좌
    print(num_list[r][c + 1])  # 우

# 벽을 세워야 한다
# 주어진 2차원 리스트의 범위를 벗어나지 않도록 제한을 두는 행위

# 1. 벽에 제한을 두는데, 벽을 넘어가는 경우, 아무것도 하지 않는다
# 2. 벽을 넘어가지 않는 경우에만 기능을 수행

N = int(input())
x = 0
y = 1

for d in range(4):
    # 다음에 이동할(탐색할) 좌표 담기
    nx = x + dx[d]
    ny = y + dy[d]

    # map 을 벗어나는 경우 아무것도 하지 않기
    if nx < 0 or nx > N or ny < 0 or ny > N:
    # if isSafeArea():
        continue

    # print(결과)
    # 특정 로직 수행

    # map 을 벗어나지 않는 경우에만 수행
    if nx > 0 or nx < N or ny > 0 or ny < N:
        # 로직 수행
        pass

def isSafeArea(nx, ny, N):
    if 0 <= nx <= N or 0 <= ny <= N:
        return True
    return False