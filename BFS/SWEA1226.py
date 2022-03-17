#미로1
from collections import deque
import sys
sys.stdin = open('SWEA1226_input.txt')

di = [-1,1,0,0]
dj = [0,0,-1,1]


def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                return (i,j)

def bfs(tup):
    Q = deque()
    Q.append(tup)
    visited[tup[0]][tup[1]] = 1
    while Q:
        v = Q.pop()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj] != 1 and visited[ni][nj] != 1:
                if arr[ni][nj] == 3:
                    return 1
                arr[ni][nj] = 1
                Q.append((ni,nj))
                visited[ni][nj] = 1
                
    return 0
        




T = 10
for tc in range(1,T+1):
    t = int(input())
    arr = [list(map(int, list(input()))) for i in range(16)]
    visited = [[0] * 16 for i in range(16)]
    
    print(f'#{tc} {bfs(find_start(arr))}')