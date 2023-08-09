# 괄호검사
T = int(input())

for test_case in range(1, T + 1):
    code = input()

    # 괄호 검사
    N = len(code)  # 문자열의 총 길이
    new_string = []  # 괄호를 담을 리스트
    top = -1

    for i in range(N):
        # 왼쪽 괄호를 만나면 push
        if code[i] == '{' or code[i] == '(':
            new_string.append(code[i])

        # 오른쪽 괄호를 만나 짝 대조
        elif code[i] == '}':
            # 리스트가 비어있으면 push
            if len(new_string) == 0:
                new_string.append(code[i])
            # 대조해서 맞으면 pop
            elif new_string[top] == '{':
                new_string.pop(top)
            # 리스트가 비어있지만 맞는 것도 없으면 push 하고 top 변경
            else:
                new_string.append((code[i]))
                top -= 1

        elif code[i] == ')':
            if len(new_string) == 0:
                new_string.append(code[i])
            elif new_string[top] == '(':
                new_string.pop(top)
            else:
                new_string.append((code[i]))
                top -= 1

    if len(new_string) >= 1:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')

