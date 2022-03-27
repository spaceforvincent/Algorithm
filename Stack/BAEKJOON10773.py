#제로
import sys

case = int(sys.stdin.readline())
stack = []
for i in range(case):
    num = int(sys.stdin.readline())
    if not stack:
        stack.append(num)
    elif num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))