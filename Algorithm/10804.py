# 문자열의 거울상
T = int(input())

for test_case in range(1, T + 1):
    arr = input()

    #값을 저장할 빈 리스트 생성
    result = []

    # 거꾸로 출력
    # 해당 글자마다 바뀐 형태 출력
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 'q':
            result.append('p')
        elif arr[i] == 'p':
            result.append('q')
        elif arr[i] == 'b':
            result.append('d')
        else:
            result.append('b')

    ans = ''.join(result)
    print(f'#{test_case} {ans}')


