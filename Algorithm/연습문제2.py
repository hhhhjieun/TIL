T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().s))

    arr = [0] * 11  # 숫자 등장 횟수 기록할 빈 리스트

    # 6자리를 순회하면서 각 인덱스 값에 횟수 추가
    for i in range(6):
        arr[num[i]] += 1  # 값이 나올 때 arr 리스트에 +1

    # tri, run 초기화
    tri = 0
    run = 0

    # 인덱스 9번까지
    j = 0
    while j < 10:
        # 갯수가 3개 이상이면 tri
        if arr[j] >= 3:
            tri += 1
            arr[j] -= 3
            continue

        # 연속되는 수가 1 이상이면 run
        if arr[j] >= 1 and arr[j + 1] >= 1 and arr[j + 2] >= 1:
            run += 1
            arr[j] -= 1
            arr[j + 1] -= 1
            arr[j + 2] -= 1
            continue

        j += 1

    # tri 와 run 의 합이 2이면 성공
    if tri + run == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')










