# 나이트의 이동
# import sys
# from collections import deque
#
# def bfs(si, sj, I):
#     visited = [[0] * I for _ in range(I)]
#     deq = deque()
#     deq.append((si, sj))
#     visited[si][sj] = 1
#
#     while deq:
#         i, j = deq.popleft()
#         if i == ei and j == ej:
#             return visited[i][j] - 1
#
#         di = [-2, -2, -1, -1, 1, 1, 2, 2]
#         dj = [1, -1, 2, -2, 2, -2, 1, -1]
#         for k in range(8):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < I and 0 <= nj < I and visited[ni][nj] == 0:
#                 deq.append((ni, nj))
#                 visited[ni][nj] = visited[i][j] + 1
#
#     return 0
#
#
# T = int(sys.stdin.readline())
#
# for test_case in range(1, T + 1):
#     I = int(sys.stdin.readline())  # 체스판 길이
#     si, sj = map(int, sys.stdin.readline().split())  # 시작점
#     ei, ej = map(int, sys.stdin.readline().split())  # 도착점
#
#     arr = [[0] * I for _ in range(I)]
#
#     result = bfs(si, sj, I)
#
#     print(result)

# 경로 찾기
# import sys
#
# def dfs(si, N, arr):
#     stack = []
#     visited = [0] * N
#
#     while True:
#         for w in range(N):
#
#             if arr[si][w] == 1 and visited[w] == 0:
#                 stack.append(si)
#                 si = w
#                 visited[si] = 1
#                 break
#         else:
#             if stack:
#                 si = stack.pop()
#             else:
#                 break
#
#     return visited
#
#
# N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 간선 정보
#
#
# for i in range(N):
#     result = dfs(i, N, arr)
#     for k in result:
#         print(k, end=' ')
#     print()

# 1로 만들기2
'''
1. x가 3으로 나누어 떨어지면, 3
2. x가 2로 나누어 떨어지면, 2
3. 1을 뺀다
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
q.append((N, [N]))
visited = [0] * (N + 1)

while q:
    num, ans = q.popleft()
    if num == 1:
        print(len(ans) - 1)
        for num in ans:
            print(num, end=' ')
        break

    if visited[num] == 0:
        visited[num] = 1
        if num % 3 == 0:
            q.append((num//3, ans + [num // 3]))

        if num % 2 == 0:
            q.append((num//2, ans + [num//2]))

        q.append((num-1, ans + [num - 1]))



