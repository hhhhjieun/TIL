# 숫자를 정렬하자
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


    # 선택 정렬 함수
    def SelectionSort(arr, N):
        for i in range(N - 1):
            min_idx = i
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr


    # 정렬된 새로운 리스트
    new_arr = SelectionSort(arr, N)

    print(f"#{test_case}", end=" ")
    [print(i, end=" ") for i in new_arr]
    print()
