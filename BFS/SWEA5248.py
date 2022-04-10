#그룹 나누기

from collections import deque

def bfs(v):
    global cnt
    Q = deque()
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.popleft()
        for w in range(1,N+1):
            if adj[v][w] == 1 and not visited[w]:
                Q.append(w)
                visited[w] = 1
    cnt += 1
                

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0] * (N+1) for i in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    
    for i in range(M):
        s, e = arr[2*i], arr[2*i+1]
        adj[s][e] = adj[e][s] = 1
    
    for i in range(1,N+1):
        if not visited[i]:
            bfs(i)
    
    print(f'#{tc} {cnt}')