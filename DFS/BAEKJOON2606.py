#바이러스
def dfs(now):
    global cnt
    visited[now] = 1 #방문체크
    
    for w in range(1,N+1):
        if adj[now][w] == 1 and visited[w] == 0 :
            cnt += 1
            dfs(w)        

import sys
from collections import deque
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s][e] = adj[e][s] = 1   
    
cnt = 0
visited = [0] * (N+1)
dfs(1)
print(cnt)