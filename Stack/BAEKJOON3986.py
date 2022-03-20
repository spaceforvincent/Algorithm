#좋은단어
#두번 연속으로 나오는 문자 제거하는 문제랑 비슷한 듯 
import sys

case = int(sys.stdin.readline())
cnt = 0
for i in range(case):
    stack = []
    string = sys.stdin.readline().rstrip()
    
    for ch in string:
        if not stack:
            stack.append(ch)
        elif stack[-1]==ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        cnt += 1

print(cnt)