
T = int(input())   # 테스트 케이스 개수

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    max_val = arr[0]  # 초기 max 값 설정
    min_val = arr[0]  # 초기 min 값 설정
    for i in range(1, N):
        if max_val < arr[i]:  # 값을 비교하여 더 큰 값을 변경
            max_val = arr[i]

        if arr[i] < min_val:  # 값을 비교하여 더 작은 값을 변경
            min_val = arr[i]

    result = max_val - min_val

    print(f'#{test_case} {result}')

