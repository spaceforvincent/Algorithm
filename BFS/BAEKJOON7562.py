#나이트의 이동

di = [-2,-2,-1,1,2,2,-1,1] #8방향 (상상좌, 상상우, 좌좌상, 좌좌하, 하하좌, 하하우, 우우상, 우우하)
dj = [-1,1,-2,-2,-1,1,2,2]

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    visited[i][j] = 1
    while Q:
        i,j = Q.popleft()
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<l and 0<=nj<l and visited[ni][nj] == 0:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

import sys
from collections import deque

T = int(sys.stdin.readline())
for tc in range(1,T+1):
    l = int(sys.stdin.readline()) #체스판 한변의 길이
    now1, now2 = map(int, sys.stdin.readline().split())
    target1, target2 = map(int, sys.stdin.readline().split())
    visited = [[0] * l for i in range(l)]

    bfs(now1, now2)
    print(visited[target1][target2]-1)