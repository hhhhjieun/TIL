# 최소합
T = int(input())

# bfs 로 완전탐색
def find_way(si, sj):

    visited[si][sj] = arr[si][sj]
    q = []
    q.append((si, sj))

    di = [1, 0]
    dj = [0, 1]

    while q:
        i, j = q.pop(0)

        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 방문한 적이 없는 곳
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    q.append((ni, nj))
                else:

                    visited[ni][nj] = min(visited[ni][nj], visited[i][j] + arr[ni][nj])


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    find_way(0, 0)

    print(f'#{test_case} {visited[-1][-1]}')




