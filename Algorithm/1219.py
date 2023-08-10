# 길찾기
T = int(input())

def dfs(n, V, adj_m):
    stack = []  # stack 생성
    result = []
    visited = [False] * (V + 1)  # visited 생성
    visited[n] = True  # 시작점 방문 표시
    result.append(n)

    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기
        for w in range(1, V + 1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(n), v = w
                n = w
                visited[n] = True  # w 방문 표시
                result.append(n)
                break  # for w, n 에 인접인 w c 찾은 경우
        else:
            if stack:  # 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop()해서 다시 다른 w를 찾을 n 준비
            else:  # 스택이 비어있으면
                break  # while Ture 탐색 끝

    return result

for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # V : 노드 개수, E : 간선 개수

    adj_m = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):  # 간선 정보
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1

    S, G = map(int, input().split())  # S: 출발 노드 , G : 도착 노드

    result = [dfs(S, V, adj_m)]

    if S in result[0] and G in result[0]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')