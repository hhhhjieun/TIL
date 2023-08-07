# 글자수
T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 카운팅할 빈 딕셔너리 생성
    cnt = {}

    for cha in str1:
        cnt[cha] = 0

    # str2에 있는 단어를 순회하면서
    for check in str2:
        # 그 단어가 str1에 있으면 값 갱신
        if check in str1:
            cnt[check] += 1

    # 최대 글자 수 출력
    max_cnt = 0
    for cha in cnt:
        if max_cnt <= cnt[cha]:
            max_cnt = cnt[cha]

    print(f'#{test_case} {max_cnt}')






