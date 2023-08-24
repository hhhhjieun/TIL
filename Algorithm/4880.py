# 토너먼트 카드게임
T = int(input())

# 이기는 경우
win = [[2, 1], [3, 2], [1, 3], [1, 1], [2, 2], [3, 3]]

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # game 함수
    def game(i, j, arr):
        if i == j:
            return i
        mid = (i + j) // 2

        # 앞쪽 플레이어
        A = game(i, mid, arr)
        B = game(mid + 1, j, arr)

        if [arr[A], arr[B]] in win:
            return A
        else:
            return B


    print(f'#{tc} {game(0, N - 1, arr) + 1}')