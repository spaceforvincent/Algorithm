#정사각형 방

from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j):
    Q = deque()
    s = []
    Q.append([i,j])
    visited[i][j] = 1
    s.append(arr[i][j])
    
    while Q:
        p = Q.pop()
        for k in range(4):
            ni = p[0] + di[k]
            nj = p[1] + dj[k] 
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and abs(arr[ni][nj] - arr[p[0]][p[1]]) == 1:
                Q.append([ni,nj])
                visited[ni][nj] = 1
                s.append(arr[ni][nj])
    
    return min(s), len(s)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * N for i in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                m, l = bfs(i,j)
                if cnt < l or cnt == l  and m < num:
                    cnt = l
                    num = m
    print(f'#{tc} {num} {cnt}')