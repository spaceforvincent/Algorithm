#Contact
from collections import deque

def bfs(v):
    ans = v
    Q = deque()    
    Q.append(v)
    visited[v] = 1

    while Q:
        p = Q.popleft()
        if visited[ans] < visited[p] or visited[ans] == visited[p] and ans < p: #가장 나중에 연락 받게 되거나 그 중에서 가장 숫자 큰 사람
            ans = p
        for w in range(1,101) :
            if adj[p][w] == 1 and visited[w] == 0: #v와 인접하고 아직 방문하지 않은 정점
                Q.append(w)
                visited[w] = visited[p] + 1

    return ans

for tc in range(1,11):
    L, S = map(int,input().split()) #데이터의 길이, 시작점
    lst = list(map(int, input().split()))
    adj = [[0] * 101 for i in range(101)]
    for i in range(0,len(lst),2):
        adj[lst[i]][lst[i+1]] = 1
    visited = [0] * 101

    print(f'#{tc} {bfs(S)}')