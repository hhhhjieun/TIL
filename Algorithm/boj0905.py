# 비밀편지
'''
A 000000
B 001111
C 010011
D 011100
E 100110
F 101001
G 110101
H 111010
'''
import sys

N = int(sys.stdin.readline())
secret = list(sys.stdin.readline().strip())

flag = True
result = ''
i = 0
while i < len(secret):
    word = ''
    for k in range(6):
        word += secret[i+k]

    i += 6

    # 비밀번호 틀린 부분 개수
    cnt = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}

    A = '000000'
    B = '001111'
    C = '010011'
    D = '011100'
    E = '100110'
    F = '101001'
    G = '110101'
    H = '111010'

    for k in range(6):
        if A[k] == word[k]:
            cnt['a'] += 1

        if B[k] == word[k]:
            cnt['b'] += 1

        if C[k] == word[k]:
            cnt['c'] += 1

        if D[k] == word[k]:
            cnt['d'] += 1

        if E[k] == word[k]:
            cnt['e'] += 1

        if F[k] == word[k]:
            cnt['f'] += 1

        if G[k] == word[k]:
            cnt['g'] += 1

        if H[k] == word[k]:
            cnt['h'] += 1

    for cha in cnt:
        if cnt[cha] >= 5:
            result += cha
            flag = True
            break

        else:
            flag = False

    if flag is False:
        break

if flag is True:
    print(result.upper())
else:
    print(len(result)+1)

