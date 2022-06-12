#게임 개발
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1 
'''

di = [-1,1,0,0]
dj = [0,0,-1,1]

import sys
N, M = map(int, sys.stdin.readline().split())

now_i, now_j, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

cnt = 0
for k in range(4):
    ni = now_i + di[k]
    nj = now_j + dj[k]
    
    if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 1: 
        now_i = ni
        now_j = nj
        cnt += 1
        arr[ni][nj] = 2
