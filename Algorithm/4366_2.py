# 정식이의 은행업무
'''
1. 2진수를 한자리씩 바꾼 값을 10진수로 저장한다
1-1. 각 자리값이 1이면 0, 0이면 1
2. 3진수를 바꾸면서 2진수를 바꾼 값에 있으면 그 값 출력
2-1 . 0,1,2 중 자기자신을 만나면 pass, 나머지 두개만 바꿔보기
'''


# 2진수를 10진수로
def bin_to_de(arr):
    global change_bin
    n = len(arr)
    result_2 = 0
    for i in range(n):
        result_2 += arr[i] * 2**(n-1-i)

    change_bin.append(result_2)


def tri_to_de(arr):
    m = len(arr)
    result_3 = 0

    for i in range(m):
        result_3 += arr[i] * 3**(m-1-i)

    return result_3


T = int(input())

for test_case in range(1, T + 1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))

    N = len(binary)  # 2진수 길이
    M = len(trinary)  # 3진수 길이

    # 2진수 각 자리마다 값 바꾸고 10 진수로 저장
    change_bin = []
    for i in range(N):
        binary1 = binary[:]
        if binary1[i] == 1:
            binary1[i] = 0
            bin_to_de(binary1)
        else:
            binary1[i] = 1
            bin_to_de(binary1)

    # print(change_bin)

    # 3진수 각 자리마다 값 바꾸고 10진수로 저장
    flag = False
    ans = 0
    for i in range(M):
        trinary1 = trinary[:]
        for j in range(3):
            # 각 자리값이 0,1,2 중 같은 값이면 pass
            if trinary1[i] == j:
                continue
            else:
                trinary1[i] = j
                result = tri_to_de(trinary1)
                if result in change_bin:
                    ans = result
                    flag = True
                    break
        if flag is True:
            break

    print(f'#{test_case} {ans}')