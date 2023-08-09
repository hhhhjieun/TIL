# 반복문자 지우기
T = int(input())

for test_case in range(1, T + 1):
    s = list(input())

    # 문자열을 계속 순회하면서
    n = len(s)
    while n > 1:
        # 연속으로 같은 글자가 나오면 pop
        for i in range(n-1):
            if s[i] == s[i+1]:
                s.pop(i+1)
                s.pop(i)
                # 길이 2개 줄이기
                n -= 2
                break
        # 끝까지 탐색했을 때 더이상 없으면 break
        if i == n - 2:
            break

    print(f'#{test_case} {n}')




