# 이진수2

T = int(input())

# 1보다 작은 10진 소수를 2진수 변환
def Bbit_float(f):
    output = ''  # 결과값 저장
    while len(output) <= 13:  # 소수점 이해 최대 13자리까지만
        f *= 2
        s = str(f).split(".")
        output += s[0]

        if s[1] == '0':
            return output

        f = float('0.' + s[1])  # 소수점으로

    return output


for test_case in range(1, T + 1):
    N = float(input())
    result = Bbit_float(N)
    # 13자리 이상 필요한 경우 overflow
    if len(result) <= 12:
        print(f'#{test_case} {result}')
    else:
        print(f'#{test_case} overflow')
