# 단어 뒤집기
# T = int(input())
#
# for test_case in range(T):
#     sen = list(input().split())
#
#     for i in range(len(sen)):
#         test = ''
#         for j in range(len(sen[i])):
#
#             test = sen[i][j] + test
#         print(test, end=' ')


# 명령 프롬프트
# N = int(input())
# cmd = [input() for _ in range(N)]
#
# # 출력할 패턴
# pattern = ''
# if N == 1:
#     print(cmd[0])
# else:
#     for j in range(len(cmd[0])):
#         result = True
#         for i in range(N - 1):
#             if cmd[i][j] == cmd[i + 1][j]:
#                 continue
#             else:
#                 result = False
#                 break
#
#         if result is True:
#             pattern += cmd[i][j]
#         else:
#             pattern += '?'
#
#     print(pattern)

# 30
# N = list(input())
#
# # 0이 없다면 30의 배수가 될 수 없음
# if '0' not in N:
#     print('-1')
#
# else:
#     # 각 자리수의 합이 3의 배수가 아닐 때,
#     total = 0
#     for i in range(len(N)):
#         total += int(N[i])
#     if total % 3 != 0:
#         print('-1')
#
#     # 각 자리수의 합이 3의 배수일 때, 내림차순
#     else:
#         N.sort(reverse=True)
#         result = ''.join(N)
#         print(result)


# 서로 다른 부분 문자열의 개수
S = input()

n = len(S)
# 생성된 부분 문자열을 넣을 빈 세트
test_set = set()

# 부분 문자열의 길이는 1부터 len(S)까지
for i in range(n+1):
    for j in range(i, n+1):
        test_set.add(S[i:j])


# 세트 개수
result = len(list(test_set))
print(result-1)














