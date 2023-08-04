# 현주의 상자 바꾸기
T = int(input())

for test_case in range(1, T + 1):
    N, Q = map(int, input().split())  # N : 상자개수 Q : 바꿀 횟수

    # 0 으로 채워진 N 개의 박스 생성
    boxes = [0] * N

    # Q 번동안 박스 번호 변경
    for i in range(Q):
        Li, Ri = map(int, input().split())
        for box in range(Li - 1, Ri):
            boxes[box] = i + 1

    result = ''
    for num in boxes:
        result = result + str(num) + ' '

    print(f'#{test_case} {result}')

