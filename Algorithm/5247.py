# 연산
from collections import deque

T = int(input())

def bfs(N, M):
    # global min_cnt
    q = deque()
    q.append([N, 0])
    visited = [0] * 1000001
    visited[N] = 1

    while q:
        result = q.popleft()
        n = result[0]
        cnt = result[1]

        for i in range(4):
            if i == 0:
                n1 = n + 1
            elif i == 1:
                n1 = n - 1
            elif i == 2:
                n1 = n * 2
            else:
                n1 = n - 10

            if n1 == M:
                return cnt + 1

            elif n1 < 1000000 and visited[n1] == 0:
                visited[n1] = 1
                q.append([n1, cnt+1])


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    ans = bfs(N, M)
    print(f'#{test_case} {ans}')