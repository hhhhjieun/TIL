# 문자열 비교
T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    # str1 이 str2 에 일치하는 부분이 있으면
    if str1 in str2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
