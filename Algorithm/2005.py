# 파스칼의 삼각형
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    '''
    첫번째 줄은 항상 1
    두번째 줄 부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 합
    '''

    # 빈 리스트 만들기
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    # 0 삭제하기
    for i in range(N):
        n = N
        j = 0
        while j < n:
            if arr[i][j] == 0:
                arr[i].pop(j)
                n -= 1
                j = 0
            else:
                j += 1

    # 합치기
    print(f'#{test_case}')
    for lst in arr:
        for num in lst:
            print(num, end=' ')
        print()












