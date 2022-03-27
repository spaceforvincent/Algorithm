#DFS와 BFS

def dfs(now):
    
    visited[now] = 1 #방문체크
    print(now, end = ' ')
    
    for w in range(1,N+1):
        if adj[now][w] == 1 and visited[w] == 0 :
            dfs(w)        

def bfs(now):
    visited = [0] * (N+1)
    Q = deque()
    Q.append(now)
    visited[now] = 1 #enque 하면서 방문체크

    while Q:
        v = Q.popleft()
        print(v, end = ' ') #deque 하면서 할일 하기
        for w in range(1,N+1):
            if adj[v][w] == 1 and visited[w] == 0 :
                Q.append(w)
                visited[w] = 1

import sys
from collections import deque
N,M,S = map(int, sys.stdin.readline().split())
adj = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s][e] = adj[e][s] = 1   
    
visited = [0] * (N+1)
dfs(S)
print()
bfs(S)