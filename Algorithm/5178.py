# 노드의 합
'''
N : 노드의 개수
M : 리프 노드의 개수
L : 값을 출력할 노드 번호
'''

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    # 완전 이진 트리
    node = [0] * (N + 1)

    # 리프 노드 채우기 == 자식이 없음 == 마지막 단계 노드
    for _ in range(M):
        i, num = map(int, input().split())
        node[i] = num

    n = N - M  # 채워야할 부모 시작점
    # 부모 채우기(거꾸로) : 자식들의 합
    for i in range(n, 0, -1):
        # 자식 2 -> 자식의 합
        if i * 2 <= N and i * 2 + 1 <= N:
            node[i] = node[i*2] + node[i*2+1]
        # 자식 1 -> 부모 == 자식
        else:
            node[i] = node[i*2]

    print(f'#{test_case} {node[L]}')

