# 배열 최소 합
'''
순열의 조합으로
[0, 1, 2] 일 때,
0행 에서 0 번 열
1행 에서 1 번 열
2행 에서 2 번 열과 같이 합을 구함
result 갱신
'''
T = int(input())


# 순열 조합
def candidate(y):
    global result  # 전역변수 사용 -> return 값 필요X

    if y == N:
        total = 0
        for ey, ex in enumerate(A):  # ey : index // ex : value
            total += arr[ey][ex]

        if result > total:  # 최솟값 갱신
            result = total

    else:
        for j in range(y, N):
            A[y], A[j] = A[j], A[y]
            candidate(y+1)
            A[y], A[j] = A[j], A[y]


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열 조합
    A = [0] * N
    for num in range(N):
        A[num] = num

    result = 10 ** 9
    candidate(0)

    print(f'#{test_case} {result}')
