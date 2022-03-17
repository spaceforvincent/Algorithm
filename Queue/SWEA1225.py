#암호 생성기
from collections import deque

for tc in range(1,11):
    t = int(input())
    Q = deque(list(map(int, input().split())))
    
    while Q[-1] != 0 :
        for i in range(1,6): 
            t = Q.popleft() 
            if t-i <= 0: 
                Q.append(0)
                break
            else:
                Q.append(t-i)
        
    
    print('#{}'.format(tc), *Q)