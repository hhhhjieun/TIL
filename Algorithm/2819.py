# 격자판의 숫자 이어 붙이기
T = int(input())


def dfs(i, j, number):
    if len(number) == 7:
        result.add(number)
        return

    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, number + arr[ni][nj])


for test_case in range(1, T + 1):
    arr = [input().split() for _ in range(4)]

    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{test_case} {len(result)}')