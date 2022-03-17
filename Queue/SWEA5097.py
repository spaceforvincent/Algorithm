#회전
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split()) #숫자 개수, 작업횟수
    
    Q = deque(list(map(int, input().split())))
    cnt = 0
    while cnt != M:
        Q.append(Q.popleft())
        cnt += 1
    
    print(f'#{tc} {Q[0]}')

