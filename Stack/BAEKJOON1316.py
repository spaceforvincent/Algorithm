#그룹단어 체커
import sys
T = int(sys.stdin.readline())
ans = 0
for t in range(1,T+1):
    stack = []
    word = list(sys.stdin.readline().rstrip())
    
    
    flag = 1
    cnt = 0
    for w in word:
        if not stack:
            stack.append(w)
            cnt += 1
        elif w != stack[-1]:
            if w in stack:
                flag = 0
                break
            else:
                stack.append(w)
                cnt = 1
        elif w == stack[-1]:
            stack.append(w)
            cnt += 1

    if flag == 1:
        ans += 1

print(ans)
        
    