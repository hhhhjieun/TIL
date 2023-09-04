# 게임을 만든 동준이
# import sys
#
# N = int(sys.stdin.readline())
#
# scores = [int(sys.stdin.readline()) for _ in range(N)]
#
# cnt = 0
# i = N - 2
# while i != -1:
#     if scores[i] >= scores[i+1]:
#         cnt += scores[i] - (scores[i+1] - 1)
#         scores[i] = scores[i+1] - 1
#     i -= 1
#
# print(cnt)

# 친구
# import sys
# from collections import deque
#
# def bfs(n):
#     q = deque()
#     visited = [0] * N
#     q.append(n)
#
#     while q:
#         i = q.popleft()
#         for w in range(N):
#             if w == i:
#                 continue
#             else:
#                 if friends[i][w] == 'Y' and visited[w] == 0:
#                     visited[w] = visited[i] + 1
#                     q.append(w)
#     cnt = 0
#     for i in range(N):
#         if i == n:
#             cnt += 0
#         else:
#             if visited[i] >= 1 and visited[i] < 3:
#                 cnt += 1
#     return cnt
#
#
# N = int(sys.stdin.readline())
# friends = [list(sys.stdin.readline().strip()) for _ in range(N)]
#
# max_friend = 0
#
# for n in range(N):
#     friend = bfs(n)
#     if max_friend < friend:
#         max_friend = friend
#
# print(max_friend)

# 통나무 건너뛰기
import sys

T = int(sys.stdin.readline())

for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())  # 통나무 개수
    trees = list(map(int, sys.stdin.readline().split()))

    trees.sort()

    grade = 0

    for i in range(2, N):
        grade = max(grade, abs(trees[i] - trees[i-2]))

    print(grade)