# 회전
T = int(input())

for test_case in range(1, T + 1):
    # N : 숫자 수, M : 회전 수
    N, M = map(int, input().split())
    cQ = list(map(int, input().split()))

    front = 0
    # 맨 앞의 숫자를 맨 뒤로 보냄 == front 를 1씩 이동
    # 회전 수 만큼 이동
    for i in range(M):
        # front 값을 조정하여 이동의 기능
        front = (front+1) % N

    print(f'#{test_case} {cQ[front]}')

    '''
    # 선형 Queue 생성
    Q = [0] * (N + M + 1)  # 충분한 저장소 만들기
    front = rear = -1

    for num in arr:
        rear += 1
        Q[rear] = num

    # 회전
    i = 0  # 회전수
    while i <= M:
        # 삭제
        front += 1
        delete = Q[front]

        # 삽입
        rear += 1
        Q[rear] = delete

        i += 1

    result = Q[rear]
    print(f'#{test_case} {result}')
    '''






