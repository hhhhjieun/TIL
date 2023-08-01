T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_val = 0
    max_val = 0
    result = 0
    # 맨 처음부터의 합계를 초기값으로 설정
    for i in range(M):
        min_val += arr[i]
    # 처음부터 끝의 M개의 개수를 뺀 순서까지
    for i in range(N - M + 1):
        total = 0
        # 해당 수부터 M개
        for j in range(i, i + M):
            total += arr[j]
        # total 비교해서 min, max 값 교체
        if total < min_val:
            min_val = total

        if max_val < total:
            max_val = total

    result = max_val - min_val

    print(f'#{test_case} {result}')