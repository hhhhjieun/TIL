# 베이비진 게임
'''
1. 두명이서 카드 나누기
2. 베이비진이 되는지 확인
3. 먼저 나오면 끝
'''

# 베이비진 확인
def baby_gin(card):
    global result
    n = len(card)
    used = [0] * n
    p = [0] * n

    def f(i, N, K):
        global result
        if i == K:
            if p[2] - p[1] == 1 and p[1] - p[0] == 1:
                result = True
            if p[2] == p[1] and p[1] == p[0]:
                result = True

        else:
            for j in range(N):
                if used[j] == 0:
                    p[i] = card[j]
                    used[j] = 1
                    f(i + 1, N, K)
                    used[j] = 0

    f(0, n, 3)
    return result


T = int(input())

for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))

    N = len(cards)

    # 카드 나누기
    card1 = []
    card2 = []
    winner = 0  # 무승부일때
    result = False

    for i in range(N):
        if i % 2 == 0:
            card1.append(cards[i])
            # 카드 3장이 넘을때, 베이비진 확인
            if len(card1) >= 3 and baby_gin(card1):
                winner = 1
                break

        else:
            card2.append(cards[i])
            if len(card2) >= 3 and baby_gin(card2):
                winner = 2
                break

    print(f'#{test_case} {winner}')
