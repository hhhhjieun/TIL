# sum
import sys
sys.stdin = open('input (1).txt')

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_total = 0
    # 가로
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]

        if total > max_total:
            max_total = total

    # 세로
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]

        if total > max_total:
            max_total = total

    # 대각선1
    total = 0
    for i in range(100):
        total += arr[i][i]

    if total > max_total:
        max_total = total

    # 대각선2
    total = 0
    for i in range(99, -1, -1):
        total += arr[i][i]

    if total > max_total:
        max_total = total

    print(f'#{tc} {max_total}')
