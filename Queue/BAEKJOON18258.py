#큐2
import sys
from collections import deque
N = int(sys.stdin.readline())

Q = deque()
for i in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        Q.append(order[1])
    elif order[0] == 'front':
        if not Q:
            print(-1)
        else:
            print(Q[0])
    elif order[0] == 'back':
        if not Q:
            print(-1)
        else:
            print(Q[-1])
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif order[0] == 'pop':
        if not Q:
            print(-1)
        else:
            print(Q.popleft()) 