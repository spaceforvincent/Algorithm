#탈주범 검거

from collections import deque

pipe = [[0,0,0,0], #상하좌우
        [1,1,1,1],
        [1,1,0,0],
        [0,0,1,1],
        [1,0,0,1],
        [0,1,0,1],
        [0,1,1,0],
        [1,0,1,0]]

di = [-1,1,0,0]
dj = [0,0,-1,1]
opp = [1,0,3,2] #상일 때는 하, 하일때는 상, 좌일때는 우, 우일때는 좌

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    visited[i][j] = 1
    cnt = 1 # 현재 위치 후보 개수

    while Q:
        i,j = Q.popleft()
        if visited[i][j] == L:
            return cnt
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and pipe[arr[i][j]][k] and pipe[arr[ni][nj]][opp[k]] : #파이프끼리 연결되어있을 때(둘 다 1일 때)
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
    
    return cnt #L까지 못갔을 때

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * M for i in range(N)]
    ans = bfs(R,C)
    print(f'#{tc} {ans}')