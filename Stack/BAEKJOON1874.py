#스택 수열
#스택에 push하는 순서는 반드시 오름차순
#push는 +, pop은 -

import sys
n = int(sys.stdin.readline())

stack = [] # 스택
answer = [] # 정답
result = [] # +,-담을 배열
compare = [] #정답과 비교용

for i in range(n):
    k = int(sys.stdin.readline())
    answer.append(k)

cnt = 1
for i in range(n):
    for j in range(cnt,n+1):
        if not stack:
            stack.append(j)
            cnt += 1
            result.append('+')
        elif stack[-1] == answer[i]:
            compare.append(stack.pop())
            result.append('-')
            break
        else:
            stack.append(j)
            cnt+=1
            result.append('+')
while stack:
    compare.append(stack.pop())
    result.append('-')

if compare == answer:
    for i in result:
        print(i)
else:
    print('NO')
