#정사각형 방

from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j):
    Q = deque()
    s = [] #경로 시작 번호, 경로 길이 체크용
    Q.append([i,j])
    visited[i][j] = 1
    s.append(arr[i][j]) 
    
    while Q:
        p = Q.pop()
        for k in range(4):
            ni = p[0] + di[k]
            nj = p[1] + dj[k] 
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and abs(arr[ni][nj] - arr[p[0]][p[1]]) == 1:
                Q.append([ni,nj])
                visited[ni][nj] = 1
                s.append(arr[ni][nj])
    
    return min(s), len(s) #경로 시작 번호, 경로 길이

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0] * N for i in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                m, l = bfs(i,j) #m : 경로 가장 길게 나오는 번호 중 가장 작은 번호, l : 경로 길이
                if cnt < l or cnt == l  and m < num: #정답 갱신(현재 정답보다 bfs 후 경로 길이가 길거나, 경로 길이 같을 때 경로 시작 번호가 더 작다면)
                    cnt = l
                    num = m
    print(f'#{tc} {num} {cnt}')