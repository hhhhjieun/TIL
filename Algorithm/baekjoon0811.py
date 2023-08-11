# 피보나치 수 4
# import sys
#
# memo = [0] * 10001
#
# N = int(sys.stdin.readline())
#
# memo[1] = 1
# for i in range(2, N+1):
#     if memo[i]:
#         continue
#     # 규칙이 i의 값은 i-2의 2배 와 i-1의 합
#     memo[i] = memo[i-2] + memo[i-1]
#
#
# print(memo[N])

# 설탕 배달
# import sys
#
# N = int(sys.stdin.readline())
#
# # 5kg 최대개수
# max_n5 = N // 5
#
# n5 = 0
# n3 = 0
# result = True
# # 최대개수 부터 내림차순으로 나머지가 3으로 나눠지면 그만
# for i in range(max_n5, -1, -1):
#     if (N - (5*i)) % 3 == 0:
#         n5 = i
#         n3 = (N - (5*i)) // 3
#         result = True
#         break
#     else:
#         result = False
#
# if result is True:
#     total = n3 + n5
#     print(total)
# else:
#     print(-1)

# 바이러스
# import sys
#
# # 1과 연결되어 있는 개수
# def dfs(s, N, adj_m):
#     stack = []
#     result = []
#     visited = [False] * (N+1)
#     visited[s] = True
#
#     while True:
#         for w in range(1, N+1):
#             if adj_m[s][w] == 1 and visited[w] is False:
#                 stack.append(s)
#                 s = w
#                 visited[w] = True
#                 result.append(s)
#                 break
#
#         else:
#             if stack:
#                 s = stack.pop()
#             else:
#                 break
#
#     return len(result)
#
#
# N = int(sys.stdin.readline())  # 컴퓨터 수
# E = int(sys.stdin.readline())  # 네트워크 수
# adj_m = [[0] * (N+1) for _ in range(N+1)]  # 네트워크 연결 정보
#
# for _ in range(E):
#     v1, v2 = map(int, sys.stdin.readline().split())
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
#
# result = dfs(1, N, adj_m)
# print(result)

# 바닥 장식
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
#
# deco = [list(sys.stdin.readline()) for _ in range(N)]
#
# total = 0  # 바닥 개수
#
# # 행 - 개수
# for i in range(N):
#     j = 0
#     while j < M:
#         if deco[i][j] != '-':
#             j += 1
#         else:
#             k = j
#             # arr[i][j]의 값이 1일 때, 연속되면 길이 +1
#             while k < M:
#                 if deco[i][k] == '-':
#                     k += 1
#                 # 0을 만나면 break
#                 else:
#                     break
#             total += 1
#             j = k + 1
#
# # 열 | 개수
# for j in range(M):
#     i = 0
#     while i < N:
#         if deco[i][j] != '|':
#             i += 1
#         else:
#             k = i
#             # arr[i][j]의 값이 1일 때, 연속되면 길이 +1
#             while k < N:
#                 if deco[k][j] == '|':
#                     k += 1
#                 # 0을 만나면 break
#                 else:
#                     break
#             total += 1
#             i = k + 1
#
# print(total)

# 파도반 수열
import sys

T = int(sys.stdin.readline())

for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())

    p = [0] * 101

    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2

    for i in range(5, N+1):
        p[i] = p[i-1] + p[i-5]

    print(p[N])




