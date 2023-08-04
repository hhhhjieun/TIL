# 빙고
# 철수 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자 빙고
call = [list(map(int, input().split())) for _ in range(5)]

# 사회자 빙고 하나의 리스트로
new_call = []
for lst in call:
    new_call.extend(lst)

# 해당 번호를 0으로 변환
def check(bingo, num):
    check_bingo = bingo
    for i in range(5):
        for j in range(5):
            if check_bingo[i][j] == num:
                check_bingo[i][j] = 0
                check_i = i
                check_j = j

                return check_bingo, check_i, check_j

# 빙고 판정하는 함수(행, 열, 대각선)
def bingo_find_r(ar):
    # 행 빙고 판정하는 함수
    rlt = 0
    for i in range(5):
        all_zero = 0
        for j in range(5):
            if ar[i][j] == 0:
                all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt

def bingo_find_c(ar):
    # 열 빙고 판정하는 함수
    rlt = 0
    for i in range(5):
        all_zero = 0
        for j in range(5):
            if ar[j][i] == 0:
                all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt


def bingo_find_cr(ar):
    # 대각선 빙고 판정하는 함수
    # 대각선 빙고의 경우 for문 밖에 all_zero를 넣어야 초기화가 안됨!!!
    rlt = 0
    all_zero = 0
    for i in range(5):
        # for j in range(5):
        if ar[i][i] == 0:
            all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt

def bingo_find_cr2(ar):
    # 대각선 빙고 판정하는 함수
    # 대각선 빙고의 경우 for문밖에 all_zero를 넣어야 초기화가 안됨
    rlt = 0
    all_zero = 0
    for i in range(5):
        # for j in range(5):
        if ar[i][4-i] == 0:
            all_zero += 1
        if all_zero == 5:
            rlt += 1
    return rlt

result = 0

for i in range(5):
    for j in range(5):
