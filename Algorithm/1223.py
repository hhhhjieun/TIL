# 계산기 2
import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())  # 길이
    arr = input()  # 식

    # 후위 표기식 변환
    stack1 = [0] * N  # N 길이 만큼 stack 생성
    postfix = ''  # 후위 표기식 저장
    icp = {'+': 1, '*': 2}  # in-coming 우선순위
    top = -1

    for token in arr:
        if token not in '+*':  # 피연산자일때
            postfix += token

        else:
            if top == -1 or icp[stack1[top]] < icp[token]:  # 우선순위가 높은 경우
                top += 1  # push
                stack1[top] = token

            elif icp[stack1[top]] >= icp[token]:  # 낮은 경우
                # stack 에 남아있는 연산자와 우선순위가 낮고 top 이 -1보다 클 때까지
                while top > -1 and icp[stack1[top]] >= icp[token]:
                    postfix += stack1[top]
                    top -= 1  # pop
                top += 1
                stack1[top] = token  # 해당 연산자 다시 push

    while top > -1:
        postfix += stack1[top]
        top -= 1

    # 후위 표기식 계산
    stack2 = []

    for token in postfix:
        if token not in '+*':
            stack2.append(int(token))

        else:
            n2 = stack2.pop()
            n1 = stack2.pop()
            if token == '+':
                stack2.append(n1+n2)
            else:
                stack2.append(n1*n2)

    print(f'#{test_case} {stack2[-1]}')





