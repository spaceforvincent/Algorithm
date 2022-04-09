#미로 탐색

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    visited[i][j] = 1
    while Q:
        i,j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and miro[ni][nj] == 1:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

from collections import deque
import sys


N, M = map(int, sys.stdin.readline().split())

miro = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]

visited = [[0] * M for i in range(N)]
bfs(0,0)

print(visited[N-1][M-1])