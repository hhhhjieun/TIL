# 중위순회
'''
배열에 저장할 상태 결정
'''
import sys
sys.stdin = open('input.txt')

def inorder(p, N):  # N : 완전 이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N)         # 왼쪽 자식으로 이동
        print(tree[p], end='')
        inorder(p*2+1, N)       # 오른쪽 자식으로 이동


T = 10

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N+1)  # N번 노드까지 있는 완전이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]

    # 중위순회
    print(f'#{test_case} ', end='')
    inorder(1, N)  # root = 1
    print()
