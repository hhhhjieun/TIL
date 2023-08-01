T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 최솟값의 인덱스
    max_idx = 0  # 최댓값의 인덱스
    for i in range(1, N):
        if arr[min_idx] > arr[i]:  # 작은 수가 여러개이면 먼저 나오는 위치
            min_idx = i

        if arr[max_idx] <= arr[i]:  # 큰 수가 여러개이면 마지막으로 나오는 위치
            max_idx = i

    ans = max_idx - min_idx
    if ans < 0: # 두 인덱스의 차가 음수이면 양수로 바꾸기
        ans = min_idx - max_idx

    print(f'#{test_case} {ans}')
