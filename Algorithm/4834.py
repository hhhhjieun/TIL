# 4834. 숫자 카드
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    max_count = 0  # 최대 갯수 초기화 값 설정
    max_num = 0  # 최대 수 초기화 값 설정

    for i in range(N):
        count = 0  # 순회하면서 같은 값일 때 갯수 초기화
        for j in range(N):
            if arr[i] == arr[j]:  # 해당 값이랑 순회하면서 돌때 값이 같으면
                count += 1  # +1

            if max_count <= count:  # count 값이 max 값 보다 크면 교체
                max_count = count
                max_num = arr[i]  # 그 때의 수 저장

            elif max_count == count:  # 만약 카드 장수가 같을 때는
                if max_num < arr[i]:  # 숫자가 큰 쪽 출력
                    max_num = arr[i]

    print(f'#{test_case} {max_num} {max_count}')