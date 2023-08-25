# 자기방으로 돌아가기
'''

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201  # 방사이 공간을 지나는 사람 수
    for a, b in arr:  # a <= b 라는 보장이 없음에 주의
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        for i in range(min(a, b+1), max(a, b)+1):
            cnt[i] += 1

    print(f'#{test_case} {max(cnt)}')

'''
'''
복도를 지나는 학생수가 단위 시간 수
복도의 구간이 겹치면 동시에 움질일 수 없으므로 단위 시간 +1
'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 돌아가야 할 학생들의 수
    # 방 사이 복도를 지나는 학생 수
    corridor = [0] * 201  # 복도 양 옆으로 방이 있으므로 복도 길이 = 방 개수 // 2

    for _ in range(N):
        a, b = map(int, input().split())
        # 짝수, 홀수 같은 복도 열에 있음
        a1 = (a + a % 2) // 2
        b1 = (b + b % 2) // 2

        if a1 > b1:
            for i in range(b1, a1 + 1):
                corridor[i] += 1

        else:
            for i in range(a1, b1 + 1):
                corridor[i] += 1


    print(f'#{test_case} {max(corridor)}')





