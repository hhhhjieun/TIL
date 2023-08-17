# 유기농 배추
'''
dfs를 통해 상하좌우에 방문한 곳이 없고 0이 나오면 cnt += 1
한곳을 탐색하고 1이 있는 다른곳으로 어떻게 이동?????
시간초과...안날까...?
'''
# import sys
# sys.setrecursionlimit(100000)
#
# T = int(input())
#
# # 상, 하, 좌, 우
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def bugs(i, j):
#     for k in range(4):
#         ny = i + dy[k]
#         nx = j + dx[k]
#
#         if 0 <= ny < N and 0 <= nx < M:
#             if cabbages[ny][nx] == 1:
#                 cabbages[ny][nx] = 0
#                 bugs(ny, nx)
#
#
# for test_case in range(1, T + 1):
#     # M : 가로, N : 세로, K : 배추 위치
#     M, N, K = map(int, input().split())
#
#     cabbages = [[0] * M for _ in range(N)]
#
#     for _ in range(K):
#         v1, v2 = map(int, input().split())
#         cabbages[v2][v1] = 1
#
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if cabbages[i][j] == 1:
#                 bugs(i, j)
#                 cnt += 1
#
#     print(cnt)

# 섬의 개수
import sys
sys.setrecursionlimit(100000)


# 상, 하, 좌, 우, 대각선
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]


def island(i, j):
    for k in range(8):
        ny = i + dy[k]
        nx = j + dx[k]

        if 0 <= ny < h and 0 <= nx < w:
            if land[ny][nx] == 1:
                land[ny][nx] = 0
                island(ny, nx)


w, h = map(int, input().split())

while w != 0 and h != 0:
    # w : 너비, h : 높이

    land = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                island(i, j)
                cnt += 1

    print(cnt)

    w, h = map(int, input().split())
