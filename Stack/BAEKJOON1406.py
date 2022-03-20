#에디터

import sys
strs = list(sys.stdin.readline().rstrip())
stack = []
order = int(sys.stdin.readline()) #명령횟수

for _ in range(order):
    something = sys.stdin.readline().split()
    act = something[0]

    if act == 'P':
        strs.append(something[1])
    elif act == 'L': #'고려'할 strs 크기를 줄이고 덜어낸 부분을 stack에 담아줌 
        if strs:
            stack.append(strs.pop())
    elif act == 'B':
        if strs:
            strs.pop()
    elif act == 'D': #stack에 담아두었던 원소들을 꺼내 담으면서 '고려'할 strs 크기를 늘림 
        if stack:
            strs.append(stack.pop())

print(''.join(strs + stack[::-1]))