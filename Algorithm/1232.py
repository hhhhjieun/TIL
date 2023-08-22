# 사칙연산
import sys
sys.stdin = open('input.txt')


def postorder(p, N):  # N : 완전 이진트리의 마지막 정점
    # 마지막 까지 들어갔을 때, 자식이 없을 때
    if not tree[p][1] and not tree[p][2]:
        # print(p)
        return tree[p][0]

    if tree[p][0] == 0:
        num1 = postorder(tree[p][1], N)  # 왼쪽 자식으로 이동
        num2 = postorder(tree[p][2], N)  # 오른쪽 자식으로 이동
        # op
        if operator[p] == '+':
            tree[p][0] = num1 + num2
        elif operator[p] == '-':
            if num1 >= num2:
                tree[p][0] = num1 - num2
            else:
                tree[p][0] = num2 - num1
        elif operator[p][0] == '*':
            tree[p][0] = num1 * num2
        else:
            if num1 >= num2:
                tree[p][0] = num1 // num2
            else:
                tree[p][0] = num2 // num1

        return tree[p][0]


T = 10

for test_case in range(1, T + 1):
    N = int(input())  # 정점의 개수
    tree = [[0, 0, 0] for _ in range(N+1)]  # 숫자
    operator = [0] * (N+1)  # 사칙 연산

    for _ in range(N):
        arr = list(input().split())  # 노드 정보
        idx = int(arr[0])

        if arr[1] not in '+-/*':
            tree[idx][0] = int(arr[1])
        else:
            operator[idx] = arr[1]
            # 자식 노드 저장
            tree[idx][1] = int(arr[2])
            tree[idx][2] = int(arr[3])

    postorder(1, N)
    result = tree[1][0]
    print(f'#{test_case} {result}')

