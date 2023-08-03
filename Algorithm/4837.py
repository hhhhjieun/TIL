# 부분집합의 합
T = int(input())

for test_case in range(1, T + 1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())

    n = 12  # 원소의 개수

    cnt_total = 0  # 원소의 합이 K인 부분집합의 개수

    for i in range(1 << n):  # 1<<n : 부분 집합의 개수
        arr = []
        total = 0  # 원소들의 합
        for j in range(n):  # 원수의 수만큼 비트 비교
            if i & (1 << j):  # i 의 j 번 비트가 1인 경우
                arr.append(A[j])
                total += A[j]

        if len(arr) == N:  # 부분집합의 길이가 N과 같을 때
            if total == K:  # 합이 K와 같을 때
                cnt_total += 1  # count +1

    if cnt_total >= 1:  # 있으면 그 갯수
        print(cnt_total)
    else:  # 없으면 0
        print(0)
