# 스택
# import sys
#
# N = int(sys.stdin.readline())
#
# # 빈 리스트(stack)
# stack = []
#
# for _ in range(N):
#     command = list(sys.stdin.readline().split())
#
#     # pop
#     if command[0] == 'push':
#         stack.append(command[1])
#     # pop
#     elif command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             pops = stack.pop(-1)
#             print(pops)
#     # size
#     elif command[0] == 'size':
#         print(len(stack))
#     # empty
#     elif command[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     # top
#     else:
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

# 요세푸스
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
#
# circle = [i for i in range(1, N + 1)]
#
# top = -1
# # 나올 순서 저장할 리스트
# out = []
# while len(circle) > 0:
#     # top을 k번째로 변경
#     top += K
#     if top > len(circle):
#         top %= len(circle)
#
#     num = circle.pop(top)
#     out.append(str(num))
#     top -= 1
#
# result = ', '.join(out)
#
# print(f'<{result}>')

# 제로
# import sys
#
# K = int(sys.stdin.readline())
#
# N = [int(sys.stdin.readline()) for _ in range(K)]
#
# arr = []
# for num in N:
#     if num != 0:
#         arr.append(num)
#     else:
#         arr.pop(-1)
#
# total = 0
# for i in arr:
#     total += i
#
# print(total)
































