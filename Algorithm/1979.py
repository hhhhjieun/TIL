# 어디에 단어가 들어갈 수 있을까?
# import sys
# sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 행 방향으로 길이만큼 연속된 1 있는지 찾기
    for i in range(N):
        # 열을 돌면서 1의 개수가 연속되면 더해서 리스트에 넣기
        y_cnt = []
        j = 0
        k = 0
        while j < N:
            if puzzle[i][j] == 0:
                y_cnt.append(puzzle[i][j])
                j += 1
            else:
                count1 = 0
                k = j
                while k < N:
                    if puzzle[i][k] == 1:
                        count1 += 1
                        k += 1
                    else:
                        break
                j = k
                y_cnt.append(count1)

        # 리스트에 K와 같은 수가 있다면 정답 += 1
        for num in y_cnt:
            if num == K:
                result += 1

    # 열 방향으로 길이만큼 연속된 1 있는지 찾기
    for j in range(N):
        x_cnt = []
        i = 0
        k = 0
        while i < N:
            if puzzle[i][j] == 0:
                x_cnt.append(puzzle[i][j])
                i += 1
            else:
                count2 = 0
                k = i
                while k < N:
                    if puzzle[k][j] == 1:
                        count2 += 1
                        k += 1
                    else:
                        break
                i = k
                x_cnt.append(count2)

        for num in x_cnt:
            if num == K:
                result += 1

    print(f'#{test_case} {result}')






