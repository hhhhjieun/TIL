# 크로아티아 알파벳
# word = input()
#
# # 크로아티아
# cros = [['c', '='], ['c', '-'], ['d', '-'], ['l', 'j'], ['n', 'j'],
#               ['s', '='], ['z', '=']]
#
# total = len(word)
#
# for i in range(total - 1):
#     test = [word[i], word[i + 1]]
#
#     for j in range(6):
#         if test == cros[j]:
#             total -= 1
#
#     if test == ['z', '=']:
#         if i >= 1 and word[i -1] == 'd':
#             total -= 2
#         else:
#             total -= 1
#
# print(total)


# 단어 공부
# word = input()
#
# # 글자를 모두 소문자로
# new_word = word.upper()
#
# # 갯수를 셀 딕셔너리 생성
# cnt = {}
# for cha in new_word:
#     cnt[cha] = 0
#
# # 갯수 세기
# for cha in new_word:
#     cnt[cha] += 1
#
# # 최대 갯수 찾기
# max_cnt = 0
#
#
# for alpha in cnt:
#     if max_cnt <= cnt[alpha]:
#         max_cnt = cnt[alpha]
#
# # 최댓값을 가진 알파벳 찾기
# result = ''
# max_num = 0
# for alpha in cnt:
#     if cnt[alpha] == max_cnt:
#         result += alpha
#         max_num += 1
#
# if max_num > 1:
#     print('?')
# else:
#     print(result)

# 그룹 단어 체커
N = int(input())

total = 0

for _ in range(N):
    word = input()

    # 갯수 세기
    word_dict = {}
    for alpha in word:
        word_dict[alpha] = 0

    for alpha in word:
        word_dict[alpha] += 1

    # 그룹으로 되어있는지 체크
    for alpha in word_dict:
        # 갯수가 1 이상일 때
        if word_dict[alpha] > 1:
            idx = 0
            for i in range(len(word)):
                if word[i] == alpha:
                    idx = i
                    break

            num = word_dict[alpha]
            for j in range(idx, idx + num):
                if word[j] == alpha:
                    total += 1
                else:
                    break

    print(total)








