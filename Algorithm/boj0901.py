# 보물
# import sys
#
# N = int(sys.stdin.readline())
#
# A = list(map(int, sys.stdin.readline().split()))
#
# B = list(map(int, sys.stdin.readline().split()))
#
#
# A.sort()
# B.sort()
#
# total = 0
# for i in range(N):
#     total += A[i] * B[N-1-i]
#
# print(total)

# A -> B
'''
2를 곱한다
1을 가장 오른쪽에 추가한다
'''
import sys

A, B = map(int, sys.stdin.readline().split())
cnt = 1

while True:
    if A == B:
        break

    elif A > B:
        cnt = -1
        break

    elif B % 2 == 0:
        B //= 2
        cnt += 1

    elif B % 10 == 1:
        B //= 10
        cnt += 1

    else:
        cnt = -1
        break

print(cnt)

