# 부분집합의 합
T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    n = 10  # 원소의 개수
    count_zero = 0
    for i in range(1 << n):  # 1<<n : 부분 집합의 개수
        total = 0  # 원소들의 합
        for j in range(n):  # 원수의 수만큼 비트 비교
            if i & (1 << j):  # i 의 j 번 비트가 1인 경우
                # print(arr[j], end=', ')
                # 부분집합의 합
                total += arr[j]
                # print(total)
                # 부분집합의 합이 0일 경우 카운트
                if total == 0:
                    count_zero += 1

    # 부분집합의 합이 있는 경우 1출력
    if count_zero >= 1:
        print(f'#{test_case} 1')
    # 없는 경우 0출력
    else:
        print(f'#{test_case} 0')



# 실습
#     def print_subset(bit, arr, n):
#         total = 0
#         for i in range(n):
#             if bit[i]:
#                 print([i], end=' ')
#                 total += arr[i]
#         print(bit, total)
#
#     arr = [1, 2, 3, 4]
#     bit = [0, 0, 0, 0]
#
#
# print_subset(bit)