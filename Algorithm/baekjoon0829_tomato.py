# 토마토
'''
위, 아래, 왼, 오, 앞, 뒤
M X N 상자 H개
익은 토마토 1, 익지 않은 토마토 0, 토마토x -1

모두 익을 때까지 걸리는 시간
이미 다 익어있는 상태 : 0 -> tomato에 0이 없는 경우
모두 익지 못하는 상황 : -1 -> 마지막에 tomato에 0이 있는 경우
'''
import sys

N, M, H = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(M*H)]

visited = [[0] * N for _ in range(M*H)]

di = [-1, 1, 0, 0, -M, M]
dj = [0, 0, -1, 1, 0, 0]


if 0 not in tomato:
    print(0)

else:
    for i in range(M):
        for j in range(N):
            for k in range(H):
                pass




