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
    # 최대 이동 거리는 k
    distance = K
    j = 0
    start = 0
    for i in range(start, N, K):
        while j < K:
            # 최대 이동거리를 이동했을 때, 충전기가 있다면
            if charge[i - j] == 1:
                start = i - j











