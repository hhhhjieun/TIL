T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))  # str은 list로 변환할 수 있음

    count = 0  # 1의 개수
    max_count = 0  # 1의 개수 최댓값

    for i in range(N):
        if arr[i] == 1:  # arr의 값이 1일 때 +1
            count += 1
        else:
            count = 0  # 0을 만나면 다시 초기화

        if max_count < count:  # 최댓값 변경
            max_count = count

    print(f'#{test_case} {max_count}')

