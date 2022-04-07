#섬의 개수

di = [-1,-1,0,1,1,1,0,-1] #상, 좌상, 좌, 좌하, 하, 우하, 우, 우상 
dj = [0,-1,-1,-1,0,1,1,1]

def bfs():
    global cnt
    Q = deque()
    while sum(sum(arr,[])) != 0: #arr 모든 원소가 0이 될때까지
        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:
                    Q.append((i,j))
                    visited[i][j] = 1
                    arr[i][j] = 0 #다시 안 세도록 섬 침몰 시키기
                    while Q:
                        i, j = Q.popleft()
                        for k in range(8):
                            ni = i + di[k]
                            nj = j + dj[k]
                            if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1:
                                Q.append((ni,nj))
                                visited[ni][nj] = 1
                                arr[ni][nj] = 0 
                    cnt += 1
    return cnt
import sys
from collections import deque
while True:
    w,h = map(int, sys.stdin.readline().split())
    if (w,h) == (0, 0):
        break
    arr = [list(map(int, sys.stdin.readline().split())) for i in range(h)]
    visited = [[0] * w for i in range(h)]
    cnt = 0

    print(bfs())