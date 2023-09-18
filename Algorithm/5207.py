# 이진 탐색
T = int(input())

def binarySearch(arr, low, high, key, last):

    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            if last == 0:
                return False
            last = 0
            return binarySearch(arr, low, mid-1, key, last)
        else:
            if last == 1:
                return False
            last = 1
            return binarySearch(arr, mid+1, high, key, last)


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    A = sorted(n)
    m = list(map(int, input().split()))

    ans = 0

    for i in range(M):
        result = binarySearch(A, 0, N-1, m[i], -1)
        if result is True:
            ans += 1

    print(f'#{test_case} {ans}')
