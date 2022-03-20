#요세푸스 문제
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
Q = deque()

for i in range(1,N+1):
    Q.append(i)

ans = []
cnt = 1
print('<', end='')
while Q:
    for i in range(M-1):
        Q.append(Q.popleft()) 
    print(Q.popleft(),end = '')
    if Q:
        print(", ", end='')
print('>')
        
