# 기차 사이의 파리
T = int(input())

for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    # 시간 = 거리 / 속력
    time = D / (A + B)

    # 거리 = 시간 * 속력
    distance = time * F

    print(f'#{test_case} {distance}')