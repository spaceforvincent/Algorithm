#단지 번호 붙이기

di = [-1,1,0,0]
dj = [0,0,-1,1]

def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                return i, j

def bfs(v):
    global ans
    cnt = 1
    Q = deque()
    Q.append(find_start())
    arr[v[0]][v[1]] = 0
    while Q :
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                cnt += 1
                Q.append((ni,nj))
                arr[ni][nj] = 0
    return cnt

import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]
ans = []
while sum(sum(arr,[])) != 0:
    ans.append(bfs(find_start()))

print(len(ans))
for i in range(len(ans)):
    print(sorted(ans)[i])
