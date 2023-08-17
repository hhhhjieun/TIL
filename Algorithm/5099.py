# 피자 굽기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N : 화덕 크기, M : 피자 개수
    Ci = list(map(int, input().split()))  # 각 피자의 치즈 양

    cQ = [0] * N  # 화덕
    front = 0
    rear = N - 1

    # 피자 넣기
    i = 0
    while i < N:
        cQ[i] = Ci[i]
        i += 1
    # 완성 피자
    result = []
    cnt = 0

    # 피자 돌리기
    while cnt <= N:
        cQ[front] = cQ[front] // 2
        if cQ[front] == 0:
            if i < M:
                cQ[front] = Ci[i]
                i += 1
                front = (front + 1) % N
                rear = (rear + 1) % N
                cnt += 1

            else:
                front = (front + 1) % N
                rear = (rear + 1) % N
                cnt += 1
        else:
            front = (front + 1) % N
            rear = (rear + 1) % N






