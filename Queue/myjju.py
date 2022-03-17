from collections import deque

Q = deque()
n = 20
Q.append((1,1))
i = 1
while n > 0 :
    t = Q.popleft()
    n-=t[1]
    Q.append((t[0],t[1]+1))
    Q.append((i+1, 1))
    i+=1

print(t)
print(len(Q))