# 고대 유적
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 긴 길이
    max_length = 0

    # 행에서 연속된 1 길이
    for i in range(N):
        j = 0
        while j < M:
            if arr[i][j] == 0:
                j += 1
            else:
                k = j
                length = 0  # 1의 개수
                # arr[i][j]의 값이 1일 때, 연속되면 길이 +1
                while k < M:
                    if arr[i][k] == 1:
                        length += 1
                        k += 1
                    # 0을 만나면 break
                    else:
                        break
                j = k + 1
                # max 갱신
                if length > max_length:
                    max_length = length

    # 열에서 연속된 1의 길이
    for j in range(M):
        i = 0
        while i < N:
            if arr[i][j] == 0:
                i += 1
            else:
                k = i
                length = 0  # 1의 개수
                while k < N:
                    if arr[k][j] == 1:
                        length += 1
                        k += 1
                    else:
                        break
                i = k + 1
                # max 갱신
                if length > max_length:
                    max_length = length

    print(f'#{test_case} {max_length}')

