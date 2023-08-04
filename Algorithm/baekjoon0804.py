# 2차원 배열의 합
# 배열의 크기 N x M
# N, M = map(int, input().split())
#
# # 배열 입력
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 합을 부분의 개수 K
# K = int(input())
#
# # i, j, x, y 입력
# for case in range(K):
#     i, j, x, y = map(int, input().split())
#     total = 0
#
#     for c in range(j - 1, y):
#         for r in range(i - 1, x):
#             total += arr[r][c]
#
#     print(total)

# 직사각형
# arr = [[0] * 100 for _ in range(100)]
#
#
# for _ in range(4):
#     x1, y1, x2, y2 = map(int, input().split())
#
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             arr[i][j] += 1
# area = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j] >= 1:
#             area += 1
#
# print(area)

# 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]

call = [list(map(int, input().split())) for _ in range(5)]

new_call = []
for lst in call:
    new_call.extend(lst)

def check(bingo, num):
    check_bingo = bingo
    for i in range(5):
        for j in range(5):
            if check_bingo[i][j] == num:
                check_bingo[i][j] = 0
                check_i = i
                check_j = j

                return check_bingo, check_i, check_j


bingo_cnt = 0
# 사회자가 번호 호출
for idx in range(len(new_call)):
    result = check(bingo, new_call[idx])
    i = result[1]
    j = result[2]

    # 같은 열, 행, 대각선으로 봤을 때,
    # 다 0 이면 bingo 수 + 1
    cnt_x = 0
    cnt_y = 0
    cnt_xy = 0
    cnt_xy2 = 0

    # 같은 행 확인(i)
    for k in range(5):
        if bingo[i][k] == 0:
            cnt_x += 1
            if cnt_x == 5:
                bingo_cnt += 1

        if bingo[k][j] == 0:
            cnt_y += 1
            if cnt_y == 5:
                bingo_cnt += 1

        for l in range(5):
            if k == l:
                if bingo[k][l] == 0:
                    cnt_xy += 1
                    if cnt_xy == 5:
                        bingo_cnt += 1

            if (4 - k) == (4 - l):
                if bingo[4 - k][4 - l] == 0:
                    cnt_xy2 += 1
                    if cnt_xy2 == 5:
                        bingo_cnt += 1


    if bingo_cnt >= 3:
        print(idx + 1)
