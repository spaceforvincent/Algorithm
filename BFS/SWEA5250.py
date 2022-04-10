#최소비용
from collections import deque

di = [1,-1,0,0]
dj = [0,0,-1,1]

def bfs(v):
    Q = deque()
    Q.append(v)
    #출발은 0 주고 시작
    visited[v[0]][v[1]] = 0
    while Q:
        i,j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N: 
                diff = 0
                if arr[ni][nj] > arr[i][j]: #다음 길이 오르막길이라면
                    diff = arr[ni][nj] - arr[i][j]
                if visited[i][j] + 1 + diff < visited[ni][nj]: #이미 저장된 비용보다 현재 경로의 계산된 비용이 덜 든다면 갱신
                    visited[ni][nj] = visited[i][j] + 1 + diff
                    Q.append((ni,nj))
        
    return visited[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [[987654321] * N for i in range(N)]
    arr = [list(map(int, input().split())) for i in range(N)]

    
    print(f'#{tc} {bfs((0,0))}')