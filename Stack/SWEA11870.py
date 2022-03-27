#괄호검사

T = int(input())
for tc in range(1,T+1):
    sentence = list(input())

    parentheses = ['(',')','{','}']
    stack = []
    for char in sentence:
        if char in parentheses:
            if not stack:
                stack.append(char)
            elif (stack[-1] == '{' and char == '}') or (stack[-1] == '(' and char == ')'):
                stack.pop()
            else:
                stack.append(char)
    if not stack:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

