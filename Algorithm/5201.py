# 컨테이너 운반
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N : 컨테이너 수, M : 트럭 수
    weigh = list(map(int, input().split()))  # N개의 화물 무게
    trucks = list(map(int, input().split()))  # M개 트럭의 적재 용량

    # 화물 무게, 트럭 용량 정렬
    weigh.sort()
    trucks.sort()

    S = []
    i = M - 1
    j = N - 1

    # 선택한 트럭의 적재 용량보다 작은 무게를 가진 화물만
    while i != -1 and j != -1:
        if trucks[i] >= weigh[j]:
            S.append(weigh[j])
            i -= 1
            j -= 1

        else:
            j -= 1

    # 무게 합
    total = 0
    for k in range(len(S)):
        total += S[k]

    print(f'#{test_case} {total}')
