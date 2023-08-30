# 전자카트
T = int(input())

# 순열
def permutation(i, N):
    # 순열 완성
    if i == N:
        ans = p[:]
        if ans[0] == 1:  # 시작점이 1일 때만
            result.append(ans)
        return

    else:
        for j in range(N):
            if used[j] == 0:  # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                permutation(i+1, N)
                used[j] = 0


for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    card = [i for i in range(1, N+1)]
    used = [0] * N
    p = [0] * N

    result = []

    permutation(0, N)

    min_total = 0
    for i in range(len(result)):
        total = 0
        for k in range(len(result[i])-1):
            total += arr[result[i][k]-1][result[i][k+1]-1]
        total += arr[result[i][-1]-1][0]
        if min_total == 0:
            min_total = total
        else:
            if min_total > total:
                min_total = total

    print(f'#{test_case} {min_total}')
