#단어 정렬

import sys

N = int(sys.stdin.readline())
ans = []

for i in range(N):
    ans.append(sys.stdin.readline().strip())
ans = list(set(ans))

ans.sort() #알파벳 순 정렬
ans.sort(key = len) #길이 순 정렬(이거 꿀인듯...)

for i in ans:
    print(i)

#시간초과 난 코드
import sys

ans = []
N = int(sys.stdin.readline())
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in ans:
        ans.append(word)

for i in range(len(ans)-1,-1,-1):
    for j in range(i):
        if len(ans[j]) >= len(ans[j+1]):
            if len(ans[j]) == len(ans[j+1]):
                for k in range(len(ans[j])):
                    if ans[j][k] > ans[j+1][k]:
                        ans[j], ans[j+1] = ans[j+1], ans[j]
                        break
                    elif ans[j][k] == ans[j+1][k]:
                        continue
                    else:
                        break    
            else:
                ans[j], ans[j+1] = ans[j+1], ans[j]
 

for i in range(len(ans)):
    print(ans[i])