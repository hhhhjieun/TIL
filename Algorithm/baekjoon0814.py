# 과제는 끝나지 않아
# import sys
#
# N = int(sys.stdin.readline())
#
# T = []  # 시간
# A = []  # 점수
# scores = 0
#
# for i in range(N):
#     task = list(map(int, sys.stdin.readline().split()))
#
#     if task[0] == 1:
#         A.append(task[1])
#         T.append(task[2])
#
#     if T:
#         time = T.pop()
#         score = A.pop()
#         time -= 1
#         if time == 0:
#             scores += score
#         else:
#             T.append(time)
#             A.append(score)
#
# print(scores)

# 단어 뒤집기2
import sys

S = sys.stdin.readline()

result = []
if '<' not in S:
    S1 = list(S.split())
    for word in S1:
        s = ''
        for char in word:
            s = char + s
        result.append(s)

        ans = ' '.join(result)

    # 문자열에 < 가 있으면
else:
    i = 0
    while i < len(S):
        s1 = ''
        if S[i] == '<':
            while S[i] != '>':
                s1 += S[i]
                i += 1

            if S[i] == '>':
                s1 += S[i]
                i += 1

            result.append(s1)

        else:
            while S[i] != '<':
                if S[i] == ' ':
                    s1 += S[i]
                    i += 1
                    break
                else:
                    s1 = S[i] + s1
                    i += 1

                if i == len(S):
                    break

            result.append(s1)

    ans = ''.join(result)

print(ans)


















