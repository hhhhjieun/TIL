# 진기의 최고급 붕어빵

# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, M, K = map(int, input().split())  # N : 손님수, M 초마다 K 개 생산
#     arr = list(map(int, input().split()))  # N명이 각각 도착하는 시간
#     arr.sort()  # 도착시간 순으로 정렬
#
#     result = 'Possible'
#     for i in range(N):
#         if i+1 > arr[i]//M*K:
#             result = 'Impossible'
#             break
#     print(f'#{test_case} {result}')


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # N명 손님, M초 마다 K개 붕어빵
    ETA = list(map(int, input().split()))  # 도착시간
    ETA.sort()

    result = 'Possible'

    for i in range(N):  # i : 흘러가는 초
        # 손님 도착 시간 // 붕어빵 시간 * 개수 이 i + 1초 보다 작으면
        if i + 1 > ETA[i] // M * K:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')



