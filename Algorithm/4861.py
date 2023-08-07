# 회문
import sys
sys.stdin = open('sample_input (2).txt')
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    word = [list(map(str, input())) for _ in range(N)]

    # 가로
    # 해당 행에서 M개씩 리스트를 만들어서 검사
    for i in range(N):
        for j in range(N - M + 1):
            # 시작 열부터 M 개의 단어를 리스트에 저장
            word_check = []
            for k in range(j, j + M):
                word_check.append(word[i][k])
            result = True
            cnt = 0
            # M // 2 만큼만 검사
            while cnt <= M // 2:
                if word_check[cnt] == word_check[M - 1 - cnt]:
                    cnt += 1
                    result = True
                else:
                    result = False
                    break

            # 모든 단어에 대해 회문이 된다면 그 단어를 출력
            if result is True:
                ans = ''.join(word_check)



    # 가로가 없다면 세로 진행
    if result is False:
        for j in range(N):
            for i in range(N - M + 1):
                word_check = []
                for k in range(i, i + M):
                    word_check.append(word[k][j])
                result = True
                cnt = 0
                while cnt <= M // 2:
                    if word_check[cnt] == word_check[M - 1 - cnt]:
                        cnt += 1
                        result = True
                    else:
                        result = False
                        break

                if result is True:
                    ans = ''.join(word_check)

    print(f'#{test_case} {ans}')

