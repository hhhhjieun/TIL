# 풍선팡
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flower = [list(map(int, input().split())) for _ in range(N)]

    # 인덱스만 합 검사
    max_total = 0
    for i in range(N):
        for j in range(M):

            # 해당 수 만큼 상하좌우 꽃가루 터짐
            n = 1
            total = flower[i][j]

            while n <= flower[i][j]:
                if 0 <= i-n:
                    total += flower[i-n][j]
                if 0 <= j-n:
                    total += flower[i][j-n]
                if i+n <= N - 1:
                    total += flower[i+n][j]
                if j+n <= M - 1:
                    total += flower[i][j+n]
                n += 1
            if max_total < total:
                max_total = total

    print(f'#{test_case} {max_total}')