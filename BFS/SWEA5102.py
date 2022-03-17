#노드의 거리
import sys
sys.stdin = open('5102_input.txt')

def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in range(1,V+1):
            if adj[v][w] == 1 and visited[w] == 0: #w가 v와 인접하고 방문하지 않은 곳일 때
                Q.append(w)
                visited[w] = visited[v] + 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for i in range(V+1)]
    visited = [0] * (V+1)
    
    for i in range(E):
        f,t = map(int, input().split())
        adj[f][t] = adj[t][f] = 1
   
    S,G = map(int, input().split())

    bfs(S)

    if visited[G] == 0:
        print(f'#{tc} {visited[G]}')
    else:
        print(f'#{tc} {visited[G]-1}')

