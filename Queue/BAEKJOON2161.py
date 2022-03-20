#카드1
import sys
from collections import deque
N = int(sys.stdin.readline())
Q = deque()
for i in range(1,N+1):
    Q.append(i)

ans = []
while len(Q) > 1:
    ans.append(Q.popleft())
    Q.append(Q.popleft())

print(*ans, *Q)