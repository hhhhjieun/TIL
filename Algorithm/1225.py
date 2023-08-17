# 암호생성기
T = 10

for test_case in range(1, T + 1):
    tc = int(input())  # test_case 번호
    cQ = list(map(int, input().split()))  # 데이터
    N = 8  # 데이터 개수

    # 원형 큐로 생각하여 front 값과 rear 값 설정
    front = 0
    rear = N - 1

    # cQ[rear]의 값이 0이하가 되면 stop
    while cQ[rear] > 0:
        # 1 - 5 까지 감소 반복 : 1 cycle
        for i in range(1, 6):
            cQ[front] = cQ[front] - i
            # 만약 i를 감소했을 때 0보다 작을 경우 break
            if cQ[front] <= 0:
                # 마지막 값이 0일 때 break -> 값 조정
                front = (front + 1) % N  # front 값 조정
                rear = (rear + 1) % N  # rear 값 조정
                break
            front = (front + 1) % N
            rear = (rear + 1) % N

    # 값이 음수일 경우가 있으므로 0으로 저장
    cQ[rear] = 0

    # front 부터 차례대로 result 에 저장
    def deq():
        global front

        result = []
        j = 0
        while j < 8:
            result.append(str(cQ[front]))
            front = (front + 1) % N
            j += 1

        return result

    result = deq()
    pw = ' '.join(result)
    print(f'#{tc} {pw}')





