# 특별한 정렬
T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))

    # 선택 정렬 함수 만들기
    def SelectionSort(arr, N):
        for i in range(N - 1):
            min_idx = i
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr

    # 정렬한 새로운 리스트 만들기
    new_arr = SelectionSort(arr, N)

    # new_arr 에 따라 특별한 정렬할 빈 리스트 생성
    result = []
    # 10개만 출력이므로 range(5)
    for i in range(5):
        result.append(new_arr[-(i + 1)])
        result.append((new_arr[i]))

    print(f"#{test_case}", end=" ")
    [print(i, end=" ") for i in result]
    print()