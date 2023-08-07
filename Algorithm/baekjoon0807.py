# 뒤집힌 덧셈
# X, Y = map(str, input().split())
#
# Rev_X = ''
# for i in X:
#     Rev_X = i + Rev_X
#
# Rev_Y = ''
# for j in Y:
#     Rev_Y = j + Rev_Y
#
# result = int(Rev_X) + int(Rev_Y)
#
# ans = ''
# for k in str(result):
#     ans = k + ans
#
# print(int(ans))

# 막대기
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# height = []
# max_height = 0
# max_idx = 0
# for num in range(N):
#     h = int(input())
#     height.append(h)
#     if max_height < h:
#         max_height = h
#         max_idx = num
#
#
# # 마지막부터 체크(오른쪽에서 봄) / 가장 큰 막대까지만 보기
# # 마지막의 막대의 높이보다 큰 것만 체크
# cnt = 1
# stick = height[-1]
#
# for i in range(N-1, max_idx - 1, -1):
#     if height[i] > stick:
#         cnt += 1
#         stick = height[i]
#
# print(cnt)

# 달팽이2
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())

# N x N 크기의 값이 0인 2차원 배열 생성
snail = [[0] * N for _ in range(M)]

num = 1  # 입력할 숫자
x, y = 0, 0  # 시작 좌표
dir = 0  # 이동방향
snail[y][x] = num  # 시작 위치에 1 기록
cnt = 0  # 꺾는 횟수


# 달팽이 반복 시작
while num < M * N:
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 다음 조사 위치가 0보다 크거나 같고, N 보다 작다면, 다음 위치가 0이면
    if 0 <= ny < M and 0 <= nx < N and snail[ny][nx] == 0:
        num += 1
        snail[ny][nx] = num
        x, y = nx, ny
    else:
        dir += 1
        cnt += 1
        if dir >= 4:
            dir = 0

print(cnt)


