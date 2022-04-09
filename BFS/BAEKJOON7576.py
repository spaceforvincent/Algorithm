#토마토

from collections import deque
import sys

di = [1,-1,0,0]
dj = [0,0,-1,1]

def check():
    global flag
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                flag = 0
                break

def start():
    global flag
    lst = []
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                flag = 1 #익은 토마토가 있긴 있음
                lst.append((i, j))
    return lst

def bfs(l):
    Q = deque()
    for a in range(len(l)):
        Q.append(l[a])
        visited[l[a][0]][l[a][1]] = 1
    
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<M and box[ni][nj] != -1 and visited[ni][nj] == 0:
                Q.append((ni,nj))
                visited[ni][nj] = 1
                box[ni][nj] = box[i][j] + 1



M,N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
flag = 0 #익은 토마토 박스에 현재 있는지 확인

bfs(start())
check() #안익은 토마토 있는지 확인

if not flag: #처음부터 익은 토마토가 아예 없었거나, -1때문에 토마토가 전부 다 익지 못한 경우
    print(-1)
else:
    print(max(sum(box,[]))-1)