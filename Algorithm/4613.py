# 러시아 국기
'''
맨 위 줄은 무조건 W
맨 아래 줄은 무조건 R
중간은 ?
'''

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 행, 열
    colors = [list(input()) for _ in range(N)]
    min_change = N * M

    # 모든 경우
    # W
    change_w = 0
    for w in range(N-2):
        for k in range(M):
            if colors[w][k] != 'W':
                change_w += 1
        # B
        change_b = 0
        for b in range(w+1, N-1):
            for k in range(M):
                if colors[b][k] != 'B':
                    change_b += 1
            # R
            change_r = 0
            for r in range(b+1, N):
                for k in range(M):
                    if colors[r][k] != 'R':
                        change_r += 1

            change = change_w + change_b + change_r

            if min_change > change:
                min_change = change

    print(f'#{test_case} {min_change}')
