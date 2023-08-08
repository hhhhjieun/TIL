# 가장 빠른 문자열 타이핑
T = int(input())


def bruteForce(pattern, target):
    N = len(target)  # 검색 대상의 길이
    M = len(pattern)  # 검색 패턴의 길이

    i = 0  # target 의 인덱스
    j = 0  # pattern 의 인덱스
    cnt = 0

    # 각 인덱스가 target 과 pattern 의 길이보다 작을동안 반복
    while i < N:
        # 패턴과 다른 곳 발견
        if target[i] != pattern[j]:
            # j 만큼 온 상태에서 틀린 곳을 발견
            # 현재 위치 - j + 1 : 다음 위치
            i = i - j
            # -1 로 j 를 초기화 하는 이유, 패턴과 일치하는 문자열이 발견 됐을 떄,
            # j + 1을 해주기 때문
            j = -1
        # 패턴과 같을 때
        i = i + 1
        j = j + 1

        if j == M:
            cnt += 1
            j = 0

    return cnt


for test_case in range(1, T + 1):
    A, B = input().split()
    cnt = bruteForce(B, A)
    a = len(A)
    b = len(B)
    result = a - ((b-1) * cnt)
    print(f'#{test_case} {result}')










