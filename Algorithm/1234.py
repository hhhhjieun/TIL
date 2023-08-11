# 비밀번호
import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    N, PW = input().split()

    pw = list(PW)
    n = int(N)

    while n > 1:
        # 연속으로 같은 글자가 나오면 pop
        for i in range(n-1):
            if pw[i] == pw[i+1]:
                pw.pop(i+1)
                pw.pop(i)
                # 길이 2개 줄이기
                n -= 2
                break

        # 연속된 글자가 없으면 끝
        else:
            for i in range(n-1):
                if pw[i] != pw[i+1]:
                    n -= 1

    result = ''.join(pw)

    print(f'#{test_case} {result}')