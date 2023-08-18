# Contact
import sys
sys.stdin = open('input.txt')

T = 10

def bfs(S):
    visited = [0] * 101  # visited 생성
    q = []  # 큐 생성
    visited[S] = 1
    q.append(S)

    while q:
        start = q.pop(0)

        for w in range(1, 101):
            if arr[start][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[start] + 1  # 거리

    return visited


for test_case in range(1, T + 1):
    N, S = map(int, input().split())  # 데이터 길이, 시작점

    contacts = list(map(int, input().split()))  # 연락망 from to

    arr = [[0] * 101 for _ in range(101)]

    for i in range(N//2):
        f, t = contacts[i*2], contacts[i*2+1]
        arr[f][t] = 1

    result = bfs(S)

    # 최대거리 중 최대수 찾기

    max_num = 0
    max_idx = 0
    for idx, num in enumerate(result):
        if num >= max_num:
            max_num = num
            max_idx = idx

    print(f'#{test_case} {max_idx}')

