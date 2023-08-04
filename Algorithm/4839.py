# 이진탐색
# 테스트 케이스
T = int(input())

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    books = list(range(1, P + 1))

    # 이진탐색 함수
    def binarySearch(arr, N, keys):
        start = 0
        end = N - 1
        cnt = 0  # 몇 번 펼치는지
        while start <= end:
            cnt += 1
            middle = (start + end) // 2
            if arr[middle] == keys:
                break
            elif arr[middle] > keys:
                end = middle
            else:
                start = middle
        return cnt

    A_cnt = binarySearch(books, P, Pa)
    B_cnt = binarySearch(books, P, Pb)

    if A_cnt > B_cnt:
        print(f'#{test_case} B')
    elif B_cnt > A_cnt:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')