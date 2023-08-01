T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 칸 넓이
    arr = list(map(int, input().split()))  # 박스가 쌓여져있는 수

# 박스가 떨어질때 같은 값이 있으면 +1

    max_num = 0
    for i in range(N):
        total = 0

        for j in arr[i:]:
            if j >= arr[i]:
                total += 1

        result = N - i - total

        if max_num < result:
            max_num = result

        print(f'#{test_case} {max_num}')


