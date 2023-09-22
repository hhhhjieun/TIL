# 장훈이의 높은 선반
T = int(input())

def backtracking(cnt, height):
    global result

    # 기저조건
    # height 가 B 이상이면 최소값 비교
    if height >= B:
        result = min(result, height)

    # 탑을 쌓은 점원 수가 N 이상이면 return
    if cnt == N:
        return

    # 점원을 쌓을 경우
    backtracking(cnt + 1, height + heights[cnt])

    # 점원을 쌓지 않을 경우
    backtracking(cnt + 1, height)


for test_case in range(1, T + 1):
    N, B = map(int, input().split())  # 점원 수, B의 높이
    heights = list(map(int, input().split()))
    result = int(1e9)
    backtracking(0, 0)
    print(f'#{test_case} {result - B}')

