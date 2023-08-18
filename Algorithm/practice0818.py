# bfs
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

'''
def bfs(s, V):  # 시작정점 : s, 마지막 정점 : V

    visited = [0] * (V+1)  # visited 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시

    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        print(t)  # 방문한 정점에서 할일
        for w in range(1, V + 1):  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_l[t][w] == 1 and visited[w] == 0:  # w 인큐, 인큐되었음을 표시
                q.append(w)
                visited[w] = 1


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_m = [[0] * (V+1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

print(adj_m)
'''
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

BFS 탐색 
> 너비 우선 탐색 // 트리같은 구조에서 노드를 탐색하는 방법 중 하나,   
> - 최단거리(경로) 문제를 풀때 용이하다. 
  - BFS의 주요 특징과, 동작과정 
    1. 시작 노드를 설정한다. 
    2. 시작노드를 Q에 삽입한다. 
    3. 큐에서 노드를 하나씩 꺼내서, 해당 노드를 방문 처리하고 출력한다. 
    4. 방금 방문한 노드의 인접한 미방문 노드를을 모두 큐에 넣는다.
    5. 큐가 빌때까지 3, 4를 반복 수행한다.  
'''
# 인접행령 -> dict
# visited -> set()

def bfs(arr, start):
    visited = set()  # 방문 여부
    queue = [start]  # 시작 노드를 큐에 삽입

    while queue:  # 큐가 빌때까지 반복
        node = queue.pop(0)  # 큐에서 노드를 하나씩 꺼낸다
        # 방문 여부 확인
        if node not in visited:  # 방문 리스트에 노드가 존재하지 않는다면,
            visited.add(node)  # 방문 처리
            print(node, end=' ')
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)


V, E = map(int, input().split())  # node, 간선
temp = list(map(int, input().split()))  # 연결 정보
graph = {}

# 간선 정보 기록하기
for i in range(E):
    graph.setdefault(temp[2*i], []).append(temp[2*i+1])
    graph.setdefault(temp[2*i + 1], []).append(temp[2*i])

'''
for i in graph:
    print(i, graph[i])
    
1 [2, 3]
2 [1, 4, 5]
3 [1, 7]
4 [2, 6]
5 [2, 6]
6 [4, 5, 7]
7 [6, 3]
'''

# 탐색 시작(인접행렬, 시작점)
bfs(graph, 1)  # 1 2 3 4 5 7 6
