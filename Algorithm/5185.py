# 이진수
T = int(input())

def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        output += "1" if i & (1 << j) else "0"

    return output

for test_case in range(1, T + 1):
    N, arr1 = input().split()

    arr = list(arr1)

    result = ''
    for i in range(len(arr)):

        if arr[i] in 'ABCDEF':
            if arr[i] == 'A':
                arr[i] = 10
            elif arr[i] == 'B':
                arr[i] = 11
            elif arr[i] == 'C':
                arr[i] = 12
            elif arr[i] == 'D':
                arr[i] = 13
            elif arr[i] == 'E':
                arr[i] = 14
            elif arr[i] == 'F':
                arr[i] = 15

        result += Bbit_print(int(arr[i]))

    print(f'#{test_case} {result}')
