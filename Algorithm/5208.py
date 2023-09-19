# 전기버스2
'''
N : 정류장 수 , M : N-1개의 정류장 별 배터리 용량
'''

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    charge = arr[1:]

    now_position = 0
    now_battery = charge[now_position]
    cnt = 0

    while True:
        # 현재 위치에서 해당 배터리로 끝까지 도달할 수 있으면 끝
        if now_position + now_battery >= N-1:
            break

        # 배터리 용량으로 갈 수 있는 곳 중에서 최대인 값으로 간다
        else:
            cnt += 1
            max_battery_position = 0
            max_position = 0

            for i in range(now_battery, -1, -1):
                if charge[now_position+i] + (now_position + i) > max_battery_position:
                    max_battery_position = charge[now_position+i] + (now_position + i)
                    max_position = now_position + i

            now_position = max_position
            now_battery = charge[now_position]

    print(f'#{test_case} {cnt}')