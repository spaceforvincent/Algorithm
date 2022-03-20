#균형잡힌 세상
import sys
while True:
    input = sys.stdin.readline().rstrip()
    if input == '.':
        break
    stack = []
    for ch in input:
        if ch in ['(',')','[',']']:
            if not stack:
                stack.append(ch)
            elif ch == '(' or ch=='[':
                stack.append(ch)
            elif ch == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    while stack and stack[-1] != '(':
                        stack.pop()
                    stack.append(ch)
            elif ch == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    while stack and stack[-1] != '[':
                        stack.pop()
                    stack.append(ch)
    if stack:
        print('no')
    else:
        print('yes')


