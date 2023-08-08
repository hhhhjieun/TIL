# 회문1
import sys
sys.stdin = open('input (1).txt')

for test_case in range(1, 11):
    N = int(input())  # 찾아야 하는 회문의 길이
    word = [input() for _ in range(8)]

    total = 0
    # 가로
    # 해당 행에서 M개씩 리스트를 만들어서 검사
    for i in range(8):
        for j in range(8 - N + 1):
            # 시작 열부터 M 개의 단어를 리스트에 저장
            word_check = []
            for k in range(j, j + N):
                word_check.append(word[i][k])
            result = True
            cnt = 0
            # M // 2 만큼만 검사
            while cnt <= N // 2:
                if word_check[cnt] == word_check[N - 1 - cnt]:
                    cnt += 1
                    result = True
                else:
                    result = False
                    break

            if result is True:
                total += 1

    # 세로
    for j in range(8):
        for i in range(8 - N + 1):
            word_check = []
            for k in range(i, i + N):
                word_check.append(word[k][j])
            result = True
            cnt = 0
            while cnt <= N // 2:
                if word_check[cnt] == word_check[N - 1 - cnt]:
                    cnt += 1
                    result = True
                else:
                    result = False
                    break

            if result is True:
                total += 1

    print(f'#{test_case} {total}')
