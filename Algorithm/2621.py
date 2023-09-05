# 카드게임
'''
카드 규칙

1. 카드 5장이 모두 같은색, 숫자 연속 -> 900 + 가장 높은 점수
2. 카드 5장 중 4장의 숫자가 같을때, 800 + 같은 숫자
3. 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때, 3장이 같은 숫자 * 10 + 2장이 같은 숫자 + 700
4. 카드 5장 모두 같은 색 -> 600 + 가장 높은 수
5. 숫자 연속 -> 500 + 가장 높은 수
6. 카드 5장 중 3장의 숫자가 같을 때, 400 + 같은 수
7. 같은 수 2장, 2장 -> 큰 수 * 10 + 300 + 작은 수
8. 2장 -> 200 + 같은 수
9. 해당 x -> 100 + 가장 큰 수

2가지 이상 규칙 적용 가능 -> 높은 점수
'''
import sys

cards = [list(sys.stdin.readline().split()) for _ in range(5)]

colors = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
nums = []
for card in cards:
    colors[card[0]] += 1
    nums.append(int(card[1]))

nums.sort()

score = 0
# 색 확인(5장이 같을 때만 존재)
re_color = ''
for color in colors:
    if colors[color] == 5:
        # 숫자가 연속적
        result = True
        for i in range(1, 5):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                result = False
                break
        if result is True:
            score += (900 + nums[-1])
        # 아닌경우
        else:
            score += (600 + nums[-1])

