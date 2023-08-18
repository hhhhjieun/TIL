# 미로2
import sys
sys.stdin = open('input.txt')

def bfs(sti, stj, N):
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append((sti, stj))  # 시작점 인큐
    visited[sti][stj] = 1  # 시작점 인큐 표시

    while q:  # 큐가 비워질때까지
        i, j = q.pop(0)  # 디큐
        if maze[i][j] == 3:  # 도착
            return 1
        # 인접하고 인큐된 적이 없으면
        # 인큐, 인큐 표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 상하좌우
            ni, nj = i + di, j + dj
            # ni, nj 가 범위 안에 있고, 값이 1이 아니고, 인큐한 적이 없을 때
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1  # 거리 표시

    return 0  # 3에 도달할 수 없는 경우


# 시작 지점
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = 10

for test_case in range(1, T + 1):
    N = 100  # 미로 크기
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(N)]  # 미로 정보

    sti, stj = find_start(N)  # 시작 지점 찾기
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')