# 부분 수열의 합
# T = int(input())
#
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     cnt = 0  # 합이 k가 되는 경우의 수
#     for i in range(1 << N):  # 부분집합을 표시하는 i
#         s = 0  # 부분집합의 합
#         for j in range(N):  # j번 비트
#             if i & (1 << j):  # i의 j번 비트검사
#                 s += arr[j]  # 0이 아니면 j번 원소가 부분집합에 포함됨
#
#         if s == K:
#             cnt += 1
#
#     print(f'#{test_case} {cnt}')

'''
def f(i, N, s, K, rs):
    global cnt
    global call

    call += 1
    if i == N:
        if s == K:
            cnt += 1

    elif s > K:
        return

    elif s+rs < K:
        return

    else:
        f(i+1, N, s+arr[i], K, rs-arr[i])
        f(i+1, N, s, K, rs-arr[i])

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    call = 0

    f(0, N, 0, K, sum(arr))
    print(f'#{test_case} {cnt} {call}')
'''

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1 << N):
        s = 0  # 부분집합의 합
        for j in range(N):  # 비트 확인
            if i & (1 << j):
                s += arr[j]

        if s == K:  # 부분집합의 합이 K와 같으면
            cnt += 1

    print(f'#{test_case} {cnt}')




