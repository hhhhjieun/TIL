# 델타 연습
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0  # total_val 의 절대값의 총합

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            total_val = 0  # val 의 총합
            for k in range(4):
                val = 0  # 상하좌우에 대한 차의 값
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:  # 배열을 벗어나지 않으면
                    s1 = arr[ni][nj]
                    if s >= s1:
                        val = s - s1
                        total_val += val
                    else:
                        val = s1 - s
                        total_val += val
                else:  # 배열을 벗어나면
                    continue

            total += total_val

    print(f'#{test_case} {total}')
