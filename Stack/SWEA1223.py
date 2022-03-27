#계산기2

T = 10
for tc in range(1, T + 1):
    L = int(input())  # 테스트케이스 길이
    lst = list(input())
    operand = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 피연산자
    stack = []  # 스택
    result = []  # 출력
 
    for i in lst:
        if i in operand:  # 피연산자라면 무조건 출력 담기
            result.append(i)
        elif i == '+':  # 더하기라면
            if not stack:  # 스택 비어있다면
                stack.append(i)
            else:  # 스택 비어있지 않다면
                while stack:  # 더하기보다 우선순위 낮은 연산자가 없으므로 다 뺴야함
                    result.append(stack.pop())
                stack.append(i)
        elif i == '*':  # 곱하기라면
            if not stack or stack[-1] == '+':  # 스택이 비어있거나 스택 탑이 +일때
                stack.append(i)  # '*'얹기 가능
            elif stack[-1] == '*':  # 스택 탑이 *일때
                while stack and stack[-1] == '*':  # 스택이 비어있지 않고 스택 꼭대기가 *인 동안
                    result.append(stack.pop())
                stack.append(i)
 
    while stack:  # 스택 비우기
        result.append(stack.pop())
 
    for i in result:
        if i in operand:
            stack.append(i)
        elif i == '+':  # 계산해서 스택에 다시 담음
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif i == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
 
    print(f'#{tc} {stack[0]}')