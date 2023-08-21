# subtree
T = int(input())

def preorder_traverse(n):
    global cnt
    if n:  # 존재하는 정점이면
        cnt += 1  # 노드 개수 + 1
        preorder_traverse(ch1[n])  # 왼쪽
        preorder_traverse(ch2[n])  # 오른쪽


for test_case in range(1, T + 1):
    E, N = map(int, input().split())  # E : 간선 개수, N : root
    V = E + 1  # 정점 수 = 간선 개수 + 1
    arr = list(map(int, input().split()))

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    # 부모 노드를 인덱스로 저장
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    # 노드 개수
    cnt = 0
    preorder_traverse(N)

    print(f'#{test_case} {cnt}')







