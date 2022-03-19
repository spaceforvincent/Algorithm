#트리의 부모 찾기
'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''

def dfs(node):
    
    visited[node] = 1
    
    for check_node in tree[node]: #node와 연결된 check node들
        if visited[check_node] == 0: #이전에 방문한적 없는 check node라면
            order[check_node] = node #node는 check_node의 부모 노드
            dfs(check_node)

import sys
sys.setrecursionlimit(10**9) #재귀 깊이 늘려주기

N = int(sys.stdin.readline())
visited = [0] * (N+1)
tree = [[] for i in range(N+1)]
order = [0] * (N+1)

for i in range(N-1):
    node1,node2 = map(int, sys.stdin.readline().split())
    tree[node1].append(node2) #둘 중 어떤게 루트인지 모름
    tree[node2].append(node1)
    
dfs(1)
for i in range(2,N+1):
    print(order[i])