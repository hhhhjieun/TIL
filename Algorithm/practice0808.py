# Target : 검색 대상 // Pattern : 검색 패턴

target = "SSAFY 10th Let's go"
pattern = "go"


def bruteForce(pattern, target):
    N = len(target)  # 검색 대상의 길이
    M = len(pattern) # 검색 패턴의 길이

    i = 0  # target 의 인덱스
    j = 0  # pattern 의 인덱스

    # 각 인덱스가 target 과 pattern 의 길이보다 작을동안 반복
    while j < M and i < N:
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
        # 패턴 인덱스 j 가 패턴의 길이만큼 탐색 된것 == 탐색 성공
        return i - M
    else:
        return - 1


# kmp 전처리
T = 'abcdabeeababcdabcef'
P = 'eaba'
def pre_process(Target):
    lps = [0] * len(Target)

    j = 0  # lps 를 만들기 위한 prefix 에 대한 idx

    '''
    i = pattern 에서 지나가는 idx
    j = 지나가고 있는 idx 와 pattern 앞 부분과 같은 곳에 대한 idx
    '''

    for i in range(1, len(Target)):
        # i & j 의 값이 같으면, lps 의 i 자리에 j + 1 을 넣음
        if Target[i] == Target[j]:
            lps[i] = j + 1
            j += 1

        # 다를 때,
        else:
            # 다르다면, 패턴의 인덱스를 초기화 한다.
            j = 0
            if Target[i] == Target[j]:
                lps[i] = j + 1
                j += 1

    return lps
lps = pre_process(T)
print(lps)

def KMP(T, P):
    lps = pre_process(T)  # SKIP TABLE 만들기

    # i = target 을 순회하는 idx
    # j = pattern 을 순회하는 idx
    i = 0
    j = 0

    # position 값이 재할당되지 않는다면, 탐색 실패를 의미
    position = -1

    # 끝까지 반복
    while i < len(T):
        # 같으면 이동 (고지식한 탐색과 같다)
        if P[j] == T[i]:
            j += 1
            i += 1
        else:
            # 다른데, j가 0이 아니라면, i 자리는 유지, j만 이동 후 탐색
            if j != 0:
                j = lps[j - 1]
            # 다른데, j 가 0 이라면, i를 한칸 이동해서 처음부터 탐색
            else:
                i += 1
        if j == len(P):
            position = i - j
            break
    return position


T = 'abcdabeeababcdabcef'
P = 'eaba'

p_idx = KMP(T, P)
print(f'p_idx : {p_idx}')

# 참고

# SKIP table
# 1. 보이어무어 패턴 검색의 장점은 검색하는 패턴의 길이만큼 스킵 가능
#    마지막 idx 를 제외할 것이다 -> pattern 의 마지막 인덱스를 검사했을 때,
#    일치하지 않는다면 len(pattern) 만큼 SKIP 할 것이다.
#    마지막에 나오는 Char는 없는 거로 취급

def pre_process(T):
    M = len(T)

    # 배열대신 딕셔너리로 Skip table 구성
    skip_t = dict()
    # 기록되지 않은 문자는 get() 메서드의 default 값을 활용할 예정
    for i in range(M - 1):
        skip_t[T[i]] = M - (1 + i)

    return skip_t

def boyer_moore(T, P):
    skip_t = pre_process(T)
    M = len(P)

    i = 0  # target idx
    while i <= len(T) - M:
        # 뒤에서부터 탐색
        # M 번째 인덱스
        j = M - 1
        # 비교를 시작할 위치
        k = (i) + (M - 1)

        # 탐색할 j idx 가 남아있고, target 과 pattern이 같으면 1씩 줄여가면서 비교
        while j >= 0 and P[j] == T[k]:
            i -= 1
            j -= 1
        # 뒤에서 부터 탐색을 하므로, j가 -1값이 된다면, 매칭이 성공했다는 뜻
        if j == -1:
            position = i
            # print(position)
            return position

        # Skip 할 곳
        # i를 비교해서 탐색을 시작할 위치에 해당하는 문자(T[i + M - 1])
        # skip_t에서 해당 문자를 찾아, 해당 문자의 Skip 값 만큼 스킵
        i += skip_t.get(T[i + M - 1], M)

    return -1



