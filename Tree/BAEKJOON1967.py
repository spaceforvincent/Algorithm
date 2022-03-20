#트리의 지름
import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
tree = [[] for i in range(N + 1)]

def dfs(v, weight):

    for i in tree[v]:
        if visited[i[0]] == -1: #방문하지 않은 노드
            visited[i[0]] = i[1] + weight
            dfs(i[0], i[1] + weight)

for i in range(N-1):
    p, c, weight = map(int, input().split()) #부모, 자식, 가중치
    tree[p].append([c, weight])
    tree[c].append([p, weight])

# 루트 노드에서 가장 먼 노드 찾기
visited = [-1] * (N + 1)
visited[1] = 0
dfs(1, 0)

# 그 노드에서 대한 가장 먼 노드 찾기
s = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[s] = 0
dfs(s, 0)

print(max(visited))