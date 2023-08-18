# 노드의 거리
T = int(input())

def bfs(S, G, V):
    visited = [0] * (V+1)  # visited 생성
    q = []  # 큐 생성
    q.append(S)  # 시작점 인큐
    visited[S] = 1  # 시작점 인큐 표시
    distance = [0] * (V+1)  # 거리

    while q:  # 큐가 비워질때까지
        start = q.pop(0)  # 디큐
        for w in range(1, V + 1):  # 가로로 탐색
            if arr[start][w] == 1 and visited[w] == 0:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
                q.append(w)
                visited[w] = 1  # 방문 표시
                distance[w] = distance[start] + 1  # 거리 += 1
                if w == G:  # 인접한 정점이 도착 정보와 같으면
                    return distance[w]

    return 0  # G에 도달할 수 없는 경우


for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # 노드 , 간선

    arr = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())  # 간선 정보
        arr[v1][v2] = 1
        arr[v2][v1] = 1

    S, G = map(int, input().split())  # 시작, 도착
    result = bfs(S, G, V)
    print(f'#{test_case} {result}')


