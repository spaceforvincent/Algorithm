from collections import deque
import sys

def bfs(v):
    global ans
    Q = deque()
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        
        for w in range(1,V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1
    

V,E = map(int, sys.stdin.readline().split())


adj = [[0] * (V+1) for i in range(V+1)]
for i in range(E):
    s, e = map(int, sys.stdin.readline().split())
    adj[s][e] = adj[e][s] = 1

visited = [0] * (V+1)

cnt = 0
for i in range(1,V+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)

