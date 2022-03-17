"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(G, v):
    queue = []
    queue.append(v)
    visited[v] = 1
    
    while queue:
        t = queue.pop(0)
        print(t, end = ' ')
        for i in G[t]:
            if visited[i] != 1:
                queue.append(i)
                visited[i] = visited[t] + 1


V, E = map(int, input().split()) #노드 개수, 간선 개수
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 초기화
visited = [0] * (V + 1)  # 방문처리
temp = list(map(int, input().split()))
ans = []
# 인접행렬 저장하기
for i in range(E): 
    s, e = temp[2 * i], temp[2 * i + 1] 
    adj[s][e] = adj[e][s] = 1  # 방향성 없음.

bfs(adj, 1)
print(visited)
