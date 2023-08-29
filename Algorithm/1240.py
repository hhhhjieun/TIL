# 단순 2진 암호코드
'''
암호코드 8개 숫자(56개)
0 : 0001101
1 : 0011001
2 : 0010011
3 : 0111101
4 : 0100011
5 : 0110001
6 : 0101111
7 : 0111011
8 : 0110111
9 : 0001011
(홀수 자리의 합 x 3) + (짝수 자리의 합) = 10의 배수
'''
import sys
sys.stdin = open('input (1).txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    # start point
    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                start_i = i
                start_j = j
                break

    # start point 에서 앞으로 56개 = code
    code = ''
    for k in range(56):
        code = arr[start_i][start_j-k] + code

    # code 7 개씩 숫자 확인
    result = []
    for i in range(0,56,7):
        number = ''
        for j in range(i, i+7):
            number += code[j]

        # number 확인
        if number == '0001101':
            result.append(0)
        elif number == '0011001':
            result.append(1)
        elif number == '0010011':
            result.append(2)
        elif number == '0111101':
            result.append(3)
        elif number == '0100011':
            result.append(4)
        elif number == '0110001':
            result.append(5)
        elif number == '0101111':
            result.append(6)
        elif number == '0111011':
            result.append(7)
        elif number == '0110111':
            result.append(8)
        else:
            result.append(9)

    # 올바른 코드 확인
    total = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5] + result[7])
    ans = sum(result)

    if total % 10 == 0:
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case} 0')


