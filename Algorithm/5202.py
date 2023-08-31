# 화물 도크
'''
s : 시작시간
e : 종료시간

1. 종료 시간이 빠른 순서로 트럭 정렬
2. 첫번째 활동(truck1)을 선택
3. 선택한 활등의 종료시간보다 빠른 시작 시간을 가진 활동 모두 제거
4. 남은 활동들에 대해 앞의 과정 반복

'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    trucks = []

    for _ in range(N):
        s, e = map(int, input().split())
        trucks.append([s, e])

    # 종료 시간이 빠른 순서로 정렬
    trucks.sort(key=lambda x: x[1])
    # print(trucks)

    # 맨 처음 시작시간 0시
    trucks = [[0, 0]] + trucks

    S = []
    j = 0

    # 선택한 활동의 종료 시간보다 느린 시작 시간을 가진 트럭만
    for i in range(1, N + 1):
        if trucks[i][0] >= trucks[j][1]:
            S.append(i)
            j = i

    # print(S)
    print(f'#{test_case} {len(S)}')



