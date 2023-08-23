# view
'''
5개씩 나눠서 탐색
더 큰 높이가 있다면 패스
작다면 그 중에서 큰 높이와의 차이
'''
import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))

    total = 0  # 총 세대 수

    # 가장자리 2자리는 탐색x
    for i in range(2, N-1):
        # 탐색할 높이
        temp = heights[i]
        min_height = temp

        # 양옆의 2개까지
        for j in range(i-2, i+3):
            # 자기자신은 pass
            if j == i:
                continue
            else:
                # 작다면 그 차이 중에서 가장 작은 차이를 +
                height = 0
                if heights[j] < temp:
                    height = temp - heights[j]
                    if height < min_height:
                        min_height = height
                # 큰 값이 있다면 높이를 0으로 변경하고 break
                else:
                    min_height = 0
                    break
        total += min_height

    print(f'#{test_case} {total}')


