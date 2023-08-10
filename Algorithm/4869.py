# 종이붙이기
T = int(input())

# N이 300까지 있기때문에 31까지 생성
memo = [0] * 31
for test_case in range(1, T + 1):
    N = int(input())
    n = N // 10  # 10의 단위는 크기때문에 //10

    memo[0] = 1
    memo[1] = 1
    for i in range(2, n+1):
        if memo[i]:
            continue
        # 규칙이 i의 값은 i-2의 2배 와 i-1의 합
        memo[i] = memo[i-2] * 2 + memo[i-1]

    print(f'#{test_case} {memo[n]}')



