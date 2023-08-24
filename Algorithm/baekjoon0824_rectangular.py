# 2527 직사각형
'''
직사각형 a
선분 b
점 c
공통부분이 없음 d
'''

import sys
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())

    # x2가 x1과 p1 사이에 존재,
    if x1 <= x2 < p1:
        # y2 or q2가 y1과 q1 사이에 있으면, -> 직사각형
        if y1 <= y2 < q1 or y1 < q2 <= q1:
            print('a')

        # y1, q1이 모두 y2와 q2 사이에 있으면 -> 직사각형
        elif y2 <= y1 <= q2 and y2 <= q1 <= q2:
            print('a')

        # y2가 q1과 좌표가 같으면 -> 선분
        elif y2 == q1 or q2 == y1:
            print('b')

        # 공통부분이 없음
        else:
            print('d')

    # x의 좌표가 경계에 있으면
    elif x2 == p1:
        if y1 < q2 <= q1 or y1 <= y2 < q1:
            print('b')
        elif y2 < q1 <= q2 or y2 <= y1 < q2:
            print('b')
        elif q2 == y1:
            print('c')
        elif y2 == q1:
            print('c')
        else:
            print('d')

    elif p2 == x1:
        if y1 < q2 <= q1 or y1 <= y2 < q1:
            print('b')
        elif y2 < q1 <= q2 or y2 <= y1 < q2:
            print('b')
        elif q2 == y1:
            print('c')
        elif y2 == q1:
            print('c')
        else:
            print('d')

    # p2가 x1과 p1 사이에 존재
    elif x1 < p2 <= p1:
        # y2 or q2가 y1과 q1 사이에 있으면, -> 직사각형
        if y1 <= y2 < q1 or y1 < q2 <= q1:
            print('a')

        # y1, q1이 모두 y2와 q2 사이에 있으면 -> 직사각형
        elif y2 <= y1 <= q2 and y2 <= q1 <= q2:
            print('a')

        # q2가 y1과 좌표가 같으면 -> 선분
        elif y2 == q1 or q2 == y1:
            print('b')

        # 공통부분이 없음
        else:
            print('d')

    else:
        if x2 < x1 < p2 and x2 < p1 < p2:
            if y1 <= y2 <= q1 and y1 <= q2 <= q1:
                print('a')
        else:
            print('d')
