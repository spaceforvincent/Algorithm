#괄호
import sys

case = int(sys.stdin.readline())
for i in range(1,case+1):
    stack = []
    parentheses = list(input())

    for o in parentheses:
        if not stack:
            stack.append(o)
        elif o == '(': #손에 쥐고 있는게 '('
            stack.append(o) 
        else: #손에 쥐고 있는게 ')'
            if stack[-1] == '(':
                stack.pop()
            else:
                while stack[-1] != '(':
                    stack.pop()
                    if not stack:
                        break
                stack.append(o)
    
    if stack:
        print('NO')
    else:
        print('YES')
    

        