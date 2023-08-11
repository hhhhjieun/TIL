# 숫자 배열 회전
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    new_arr = [[0] * 3 for _ in range(N)]

    # 90도 : new_arr 의 0열
    for j in range(N):  # 열
        result_1 = ''
        for i in range(N-1, -1, -1):  # 행
            result_1 += arr[i][j]

        new_arr[j][0] = result_1

    # 180도 : new_arr 의 1열
    for i in range(N-1, -1, -1):
        result_2 = ''
        for j in range(N-1, -1, -1):
            result_2 += arr[i][j]

        new_arr[N-1-i][1] = result_2

    # 270도 : new_arr 의 2열
    for j in range(N-1, -1, -1):
        result_3 = ''
        for i in range(N):
            result_3 += arr[i][j]

        new_arr[N-1-j][2] = result_3

    print(f'#{test_case}')
    for i in range(N):
        for j in range(3):
            print(new_arr[i][j], end =' ')
        print()







