# 간단한 소인수분해
'''
1. 해당 수에서 2, 3, 5, 7, 11 중에 나머지가 0 인 수로 나누고 해당 수 count
2. 몫을 다시 저장
3. 몫이 0 이 될 때 까지 반복
'''
# 테스트 케이스
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = 0  # 2의 개수
    b = 0  # 3의 개수
    c = 0  # 5의 개수
    d = 0  # 7의 개수
    e = 0  # 11의 개수

    n = N

    while n > 1:
        if n % 2 == 0:
            n = n // 2
            a += 1
        elif n % 3 == 0:
            n = n // 3
            b += 1
        elif n % 5 == 0:
            n = n // 5
            c += 1
        elif n % 7 == 0:
            n = n // 7
            d += 1
        elif n % 11 == 0:
            n = n // 11
            e += 1

    print(f'#{test_case} {a} {b} {c} {d} {e}')


