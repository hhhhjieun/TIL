# 쇠막대기 자르기
T = int(input())

for test_case in range(1, T + 1):
    brackets = input()

    n = len(brackets)

    stick = 0  # 막대기 총 개수
    sticks = []
    i = 0
    while i < n:
        # 막대기 개수 세기 & )를 만났을 때 없어질 수 있도록 push
        if brackets[i] == '(' and brackets[i+1] != ')':
            sticks.append(brackets[i])
            stick += 1
            i += 1

        # 레이저인지 아닌지 판별 -> (, ) 연속으로 존재
        elif brackets[i] == '(' and brackets[i+1] == ')':
            stick += len(sticks)
            i += 2  # 자리 이동

        # ) 만나면 ( 삭제, 레이저 만났을 때 늘어나는 막대 개수 조절
        elif brackets[i] == ')':
            sticks.pop(-1)
            i += 1

    print(f'#{test_case} {stick}')