import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    global ans
    visited[v] = 1

    for w in range(1,V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)
            

V,E = map(int, sys.stdin.readline().split())


adj = [[0] * (V+1) for i in range(V+1)]
for i in range(E):
    s, e = map(int, sys.stdin.readline().split())
    adj[s][e] = adj[e][s]= 1

visited = [0] * (V+1)

cnt = 0
for i in range(1,V+1):
    if not visited[i]:
       dfs(i)
       cnt += 1

print(cnt)