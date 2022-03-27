def priority(c):
    if c == '(': return 0
    elif c == '+' or c == '-': return 1
    elif c == '*' or c == '/': return 2
 
def infix_to_postfix(infix):
    stack = []
    result = []
    for ch in infix:
        # 피연산자
        if '0' <= ch <= '9':
            result.append(ch)
        # 왼쪽괄호
        elif ch == '(':
            stack.append(ch)
        # 오른쪽괄호 : ( 나올 때까지 pop -> result
        elif ch == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # 왼쪽괄호 버리기
        # 사칙연산자
        else:
            if stack: # 비어있지않으면
                # 토큰 <= stack[-1] : 낮은거 나올 때까지 pop
                while priority(ch) <= priority(stack[-1]):
                    result.append(stack.pop())
                    if len(stack) == 0: break
            stack.append(ch)  # 비어있으면, 토큰> stack[-1]
 
    #스택에 값이 남아 있으면
    while stack:
        result.append(stack.pop())
 
    return ''.join(result)  # list -> str
 
def cal(post_fix):
    stack = []
    for ch in post_fix:
        # 피연산자 : push
        if '0' <= ch <= '9':
            stack.append(int(ch))
        # 연산자 : 2개 pop -> 계산 - > push
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if ch == '+':
                stack.append(op1 + op2)
            elif ch == '-':
                stack.append(op1 - op2)
            elif ch == '*':
                stack.append(op1 * op2)
            elif ch == '/':
                stack.append(op1 / op2)
    return stack.pop()
 
T = 10
for tc in range(1, T+1):
    N = int(input())  # 수식의 길이
    infix = input()   # 중위식
    post_fix = infix_to_postfix(infix)
    # print(post_fix)
    print(f'#{tc} {cal(post_fix)}')
