# 극장 좌석
import sys

N = int(sys.stdin.readline())  # 좌석수
M = int(sys.stdin.readline())  # 고정석 개수
vip = [int(sys.stdin.readline().strip()) for _ in range(M)]

def fibo(N):
    global memo
    for i in range(N):
        if memo[i] == 0:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[N-1]

if N >=2 and N != M:
    memo = [0] * N
    memo[0] = 1
    memo[1] = 2

    stack = []
    if 1 not in vip:
        vip.insert(0, 0)
    if N not in vip:
        vip.append(N+1)
    for i in range(len(vip)-1):
        if vip[i+1]-vip[i]-1 > 0:
            stack.append(vip[i+1]-vip[i]-1)

    cnt = 1
    for i in range(len(stack)):
        result = fibo(stack[i])
        cnt *= result

    print(cnt)


elif N == 1:
    print(1)
elif N == M:
    print(1)

