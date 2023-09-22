# 창용 마을 무리의 개수
T = int(input())


def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    p[find_set(y)] = find_set(x)


for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    p = [i for i in range(N+1)]

    for _ in range(M):
        parent, child = map(int, input().split())
        union(parent, child)

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{test_case} {len(result)}')