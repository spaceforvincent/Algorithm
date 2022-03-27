#유기농 배추
import sys
from collections import deque
di = [-1,1,0,0]
dj = [0,0,-1,1]

def find_start():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1:
                return i, j
def bfs(v):
    global ans
    Q = deque()
    Q.append(v)
    arr[v[0]][v[1]] = 0
    while Q :
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<H and 0<=nj<W and arr[ni][nj] == 1:
                Q.append((ni,nj))
                arr[ni][nj] = 0
    ans += 1

T = int(sys.stdin.readline())
for tc in range(1,T+1):
    W,H,K = map(int, sys.stdin.readline().split()) #가로, 세로, 1 개수
    arr = [[0] * (W) for i in range(H)]
    ans = 0
    for i in range(K):
        s, e = map(int, sys.stdin.readline().split())
        arr[e][s] = 1
    
    while sum(sum(arr,[])) != 0:
        bfs(find_start())

    print(ans)
    