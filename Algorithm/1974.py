# 스토쿠 검증
T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = True

    # 가로
    # 각 열을 순회하면서 각 숫자를 빈 리스트에 넣기
    for i in range(9):
        num1 = [0] * 10
        for j in range(9):
            num1[arr[i][j]] += 1

        # 1-9 의 값이 1이면 패스, 그 값이 1 이 아니면 False
        for k in range(1, 10):
            if num1[k] != 1:
                result = False
                break

    # 세로
    for j in range(9):
        num2 = [0] * 10
        for i in range(9):
            num2[arr[i][j]] += 1

        for k in range(1, 10):
            if num2[k] != 1:
                result = False
                break

    # 3 * 3
    for i in range(0, 6, 3):
        for j in range(0, 6, 3):
            num3 = [0] * 10
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    num3[arr[k][l]] += 1

            for n in range(1, 10):
                if num3[n] != 1:
                    result = False
                    break

    if result is False:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')