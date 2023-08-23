# 행렬찾기
'''
용기 내에는 빈 용기가 없으므로 0이 아닌 값까지 행, 열 카운트
'''
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    containers = [list(map(int, input().split())) for _ in range(n)]

    contain = 0  # 용기 개수

    