# sum
import sys
sys.stdin = open('input.txt')
from pprint import pprint as pp

# 10개의 test_case
for i in range(1, 11):
    # 100개의 행의 값 입력
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_total = 0
    # 각 행의 합
    for c in range(100):
        total_c = 0  # 각 행의 합 초기화
        for r in range(100):
            total_c += arr[c][r]

            # 만약 max_total 보다 크다면 max_total 변경
            if max_total < total_c:
                max_total = total_c

    # 각 열의 합
    for r in range(100):
        total_r = 0  # 각 열의 합 초기화
        for c in range(100):
            total_r += arr[c][r]

            # 만약 max_total 보다 크다면 max_total 변경
            if max_total < total_r:
                max_total = total_r

    # 대각선의 합
    total_cr1 = 0
    for c in range(100):
        for r in range(100):
            if c == r:
                total_cr1 += arr[c][r]

                if max_total < total_cr1:
                    max_total = total_cr1

    total_cr2 = 0
    for c in range(99, -1, -1):
        for r in range(99, -1, -1):
            if c == r:
                total_cr2 += arr[c][r]

                if max_total < total_cr2:
                    max_total = total_cr2

    print(f'#{test_case} {max_total}')




