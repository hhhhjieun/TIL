# 최소 생산 비용
'''
N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산
백트래킹으로 1-N의 부분집합을 구해서
합을 더하고 부분집합의 길이가 N일 때 최솟값 갱신
'''
T = int(input())


def backtracking(cnt, i, total):
    global min_cost

    if total >= min_cost:
        return

    # 길이가 N이 되면 최솟값 비교
    if cnt == N:
        # print(total)
        # print(path)
        if total < min_cost:
            min_cost = total

    # 반복문
    for w in range(N):
        if path[w] == 0:
            # 들어가기 전 로직 - 경로 저장 & total 계산
            path[w] = 1
            total += cost[cnt][w]
            # 다음 재귀 호출
            backtracking(cnt + 1, w, total)
            # 로직 후 초기화
            path[w] = 0
            total -= cost[cnt][w]


for test_case in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 10000000

    for i in range(N):
        path = [0] * N
        path[i] = 1
        total = cost[0][i]
        backtracking(1, i, total)

    print(f'#{test_case} {min_cost}')
