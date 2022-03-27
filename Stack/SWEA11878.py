def cal(postfix):
    stack = []
    for ch in postfix:
        # 피연산자 : push
        if ch.isnumeric():
            stack.append(int(ch))
        # 연산자 : 2개 pop -> 계산 - > push
        elif ch in ['+','-','*','/']:
            if len(stack) < 2:
                return "error"
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
                    stack.append(op1 // op2)
        elif ch =='.':
            if len(stack) != 1:
                return "error"
            else:
                return stack.pop()
    print(stack)
 
T = int(input())
for tc in range(1, T+1):
    postfix = input().split()   # 후위식
    print(f'#{tc} {cal(postfix)}')
