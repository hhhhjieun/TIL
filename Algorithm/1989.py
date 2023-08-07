# 초심자의 회문 검사
T = int(input())

for test_case in range(1, T + 1):
    word = input()

    # 단어의 길이 // 2 만큼 비교
    length = len(word)
    i = 0  # 비교할 인덱스 번호
    result = True  # 반환할 값
    while i <= length // 2:
        # 대칭되는 인덱스의 값이 같으면
        if word[i] == word[length - 1 - i]:
            i += 1
            result = True
        # 다르면 break
        else:
            result = False
            break

    if result is True:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
