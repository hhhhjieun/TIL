# 백만 장자 프로젝트
'''
N 날동안 최대값 찾기
마지막 날은 살 수 없기때문에 최대값을 마지막날로 초기값 설정
오른쪽에서부터 비교하면서 작으면 그 차이 계산
크면 최대값 갱신, 이후 계속 진행
'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]  # 초기 max 값을 마지막날로 설정
    total = 0  # 이익

    # 오른쪽에서 부터 최대값보다 작으면 사서 그 차이를 계산
    for i in range(N-2, -1, -1):
        # 최대값보다 더 크면 최대값 갱신
        if price[i] > max_price:
            max_price = price[i]
        else:
            total += (max_price - price[i])

    print(f'#{test_case} {total}')


