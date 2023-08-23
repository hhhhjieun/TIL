'''
# 트리 만들기

import sys

n, m = map(int, sys.stdin.readline().split())

# 자식 노드 표
children = [[0] * n for _ in range(n)]

# 루트 0에서 m까지 간선 연결
for i in range(1, m+1):
    children[0][i] = 1


cnt = m+1
node = 1
while cnt < n:
    children[node][cnt] = 1
    node += 1
    cnt += 1

for i in range(n):
    for j in range(n):
        if children[i][j] == 1:
            print(i, j)
'''

# 부동산 다툼
import sys
N, Q = map(int, sys.stdin.readline().split())  # N : 땅, Q : 오리
land = [0] * (N+1)  # 이진 트리 땅

for i in range(Q):
    xi = int(sys.stdin.readline())  # 오리가 원하는 땅

    # 부모 노드가 1이 아니면 값 입력
    p = xi // 2
    result = []

    if land[xi] == 1:
        result.append(xi)

    while p > 0:
        if land[p] == 1:
            result.append(p)
            p = p // 2
        else:
            p = p // 2

    if result:
        print(result[-1])
    else:
        land[xi] = 1
        print(0)




