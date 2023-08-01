# 전기 버스
T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # N개의 정류장
    charge = [0] * N

    # 충전기가 있으면 값 1
    for i in range(M):
        charge[arr[i]] += 1

    # 버스 출발

    j = 0
    start = 0
    count = 0
    i = 0

    while i <= N:
        while j < K:
            # 최대 이동거리를 이동하는 동안, 충전기가 있다면
            if charge[i + K - j] == 1:
                i = i + K - j
                count += 1
                break

            else:
                j += 1

    print(count)









