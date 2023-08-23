# Ladder1
T = 10

for test_case in range(1, T + 1):
    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 시작점 찾기
    idx = 0
    while ladder[99][idx] != 2:
        idx += 1

    # 사다리타기
        # 상, 좌, 우
    dy = [-1, 0, 0]
    dx = [0, -1, 1]

    start = idx
    for i in range(98, 0, -1):
        for j in range(99):
            pass