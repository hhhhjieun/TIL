# 색칠하기
from pprint import pprint as pp
# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]

    # 빈 10x10 격자 만들기
    m = 10
    n = 10

    arr = []
    for i in range(n):
        row = [0] * m
        arr.append(row)


    # 각 리스트의 마지막 값에 따라
    for red_lst in color:
        #빨강(1)
        if red_lst[-1] == 1:
            # 행 - 열 위치 따라서 1로 변경
            for i in range(red_lst[0], red_lst[2] + 1):
                for j in range(red_lst[1], red_lst[3] + 1):
                    arr[i][j] += 1


       # 파랑(2)
        else:
            for i in range(red_lst[0], red_lst[2] + 1):
                for j in range(red_lst[1], red_lst[3] + 1):
                    arr[i][j] += 2

    # 보라색(3) 개수
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{test_case} {cnt}')
