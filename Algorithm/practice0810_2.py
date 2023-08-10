'''
7 8  V E
1 2 1 3 2 4 2 4 4 6 5 6 6 7 3 7  # 간선 정보
'''

# 인접 행렬 생성

V, E = map(int, input().split())  # 노드, 간선

data = list(map(int, input().split()))  # 간선 정보

arr = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 초기화

visited = [0] * (V + 1)  # 노드의 방문 여부 체크 리스트
# visited = [False] * (V + 1)

# visited[n] = 1
# visited[n] = True

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    arr[n1][n2] = 1  # n1 과 n2 는 서로 인접해있다.
    arr[n2][n1] = 1



''' 
arr
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1],
 [0, 0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 1, 0, 1],
 [0, 0, 0, 1, 0, 0, 1, 0]]
'''
# 재귀
def dfs(v):
    visited[v] = 1
    print(v, end=' ')  # 특정 로직을 수행하는 곳
    # V 현재 시작정점, 인접한 정점 중에서 방문을 하지 않은 곳
    for w in range(1, V + 1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)
        else:
            v



dfs(1)

# 반복문
def dfs2(v):
    stack = [v]  # 스택 초기화
    # 스택이 빌 때까지 반복
    while len(stack):
        v = stack.pop()
        visited[v] = 1

        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:
                stack.append(w)
                print(w, end = ' ')


