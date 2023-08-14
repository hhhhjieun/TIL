# 계산기
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = input()
    num = []  # 숫자만 넣을 리스트

    # 숫자는 짝수 인덱스에 존재
    for i in range(N//2 +1):
        num.append(arr[2*i])

    total = 0  # 계산
    for n in num:
        total += int(n)

    print(f'#{test_case} {total}')

