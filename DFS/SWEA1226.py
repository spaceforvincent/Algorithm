#미로1

import sys
sys.stdin = open('input.txt')

def find_start(arr,N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j

def dfs(i,j):
    global flag
    # 방문체크
    visited[i][j] = 1
    #3에 도착했나?
    if arr[i][j] == 3:
        flag = 1
        return
    #4방향 탐색

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if visited[ni][nj] == 1:
            continue #방문한 좌표면은 다음번 방향으로 가라
        if arr[ni][nj] == 1:
            continue #벽이면은 다음번 방향으로 가라
        if 0<=ni<N and 0<=ni<N:
            dfs(ni,nj)

di = [-1,1,0,0]
dj = [0,0,-1,1]    
N = 16
T = 10
for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for i in range(N)]
    si, sj = find_start(arr,N)
    flag = 0
    dfs(si,sj)
    print(f'#{tc} {flag}')
