#ABCDE
import sys
def dfs(v, cnt):
    global flag
 
    if cnt == 4:
        flag = 1
        return

    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w, cnt +1)
            visited[w] = 0        
                    
N, M = map(int, sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)] 
for i in range(M):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (N+1)
flag = 0
for i in range(N):
    visited[i] = 1
    dfs(i,0)
    visited[i] = 0
print(flag)