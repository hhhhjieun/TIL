# 최대 상금
# 1. 메모이제이션 -> 중복된 것을 검사하지 않기 위해
# set()

import sys

T = int(input())

def swap(P, i, j):
    # 숫자 P i번째 자리랑 j번째 자리를 바꾸는 함수
    arr = [0] * N
    for k in range(N-1, -1, -1):  # P 숫자를 자리수별로 구분해서 arr에 저장
        arr[k] = P % 10
        P //= 10

    arr[i], arr[j] = arr[j], arr[i]  # 자리 바꾸기(i 번째, j번째)

    # arr 를 숫자로 변환
    P = 0
    for k in range(N):
        P = P * 10 + arr[k]

    return P


def search(P, repeat):
    global ans
    for i in range(MAXSIZE):
        # 자리를 바꿨을 때, 기입된 패턴이 없을 때,
        if memo[repeat][i] == 0:
            memo[repeat][i] = P  # 패턴 저장
            break
        elif memo[repeat][i] == P:
            return

    # 주어진 교환 횟수를 다 사용했을 때,
    if repeat == r:
        if P > ans:
            ans = P
    else:  # 교환 횟수가 남아있을 때,
        for i in range(N-1):
            for j in range(i+1, N):
                search(swap(P, i, j), repeat + 1)


MAXSIZE = 720  # 6!
for test_case in range(1, T + 1):
    memo = [[0] * MAXSIZE for _ in range(11)]
    P, r = map(int, input().split())  # 숫자 패턴 P, 교환 횟수 r
    N = len(str(P))  # 숫자 카드의 길이

    ans = 0
    search(P, 0)

    print(f'#{test_case} {ans}')

# 2. set()
# 완전탐색 // 가지치기

# 완전 탐색 활용 (가지치기)
def back_track(k):                      # k -> 교환 횟수
    global ans
    val = int(''.join(cards))           # 숫자 카드
    if val in visited[k]:               # 이미 체크 했다면 종료
        return
    visited[k].add(val)                 # 아니라면 해당 카드 조합을 추가

    if k == cnt:                        # 모든 카드를 교환 했다면(주어진 횟수만큼 교환)
        ans = max(ans, val)             # 최대 금액을 갱신
    else:
        # 카드 조합 -> 최댓값 갱신
        for i in range(num_of_cards-1):
            for j in range(i+1, num_of_cards):
                cards[i], cards[j] = cards[j], cards[i]  # 변경하고
                back_track(k+1)                          # 다음 확인
                cards[i], cards[j] = cards[j], cards[i]  # 원복


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    cards, cnt = list(arr[0]), int(arr[1])  # cards: 카드 목록, cnt: 최대 교환 횟수
    num_of_cards = len(cards)               # 카드 숫자(최대 자릿수 6)
    visited = [set() for _ in range(11)]    # 최대 10회 교환 -> 체크한 숫자 조합 파악 -> set을 활용한 중복 제거
    ans = 0
    back_track(0)   # 0번부터 시작
    print(f'#{tc} {ans}')





