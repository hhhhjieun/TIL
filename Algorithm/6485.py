# 삼성시의 버스 노선
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    AB = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    C = [int(input()) for _ in range(P)]

    # 0으로 초기화 된 5001 개의 리스트 생성
    bus_stops = [0] * 5001

    # A-B 까지 +1
    for bus in AB:
        for i in range(bus[0], bus[1] + 1):
            bus_stops[i] += 1

    bus_stop = []
    for stop in C:
        bus_stop.append(str(bus_stops[stop]))

    result = ' '.join(bus_stop)

    print(f'#{test_case} {result}')





