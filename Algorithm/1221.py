# GNS
import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    tc, N = map(str, input().split())

    arr = list(map(str, input().split()))

    # 카운팅 할 빈 딕셔너리 생성
    cnt = {
        'ZRO': 0, 'ONE': 0,
        'TWO': 0, 'THR': 0,
        'FOR': 0, 'FIV': 0,
        'SIX': 0, 'SVN': 0,
        'EGT': 0, 'NIN': 0
    }

    # 문자열 돌면서 몇개인지 세기
    for cha in arr:
        cnt[cha] += 1

    print(f'#{test_case}')

    # cnt 의 작은 수 부터 0이 될때까지 그 수만 출력
    for num in cnt:
        while cnt[num] > 0:
            print(num, end=' ')
            cnt[num] -= 1
    print()

