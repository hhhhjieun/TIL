# 삼각형 만들기
import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(1, N//3+1):
    for j in range(i, max(i, N-i)):
        k = N - i - j
        if k > j:
            break
        if i + j > k:
            cnt += 1

print(cnt)