#Two dots

#주로 델타는 bfs랑 합쳐서 많이 사용했었는데 dfs랑 결합하는건 거의 없었던 것 같아 새로웠다...

di = [-1,1,0,0]
dj = [0,0,1,-1]
import sys

def dfs(alpha, i, j, cnt, si,sj):
    global flag
    #가지치기
    if flag:
        return
    
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M:
            if cnt >= 4 and ni == si and nj == sj: #점이 4개 이상이고, ni, nj가 출발점으로 돌아왔을 때
                flag = 1
                return
            if arr[ni][nj] == alpha and visited[ni][nj] == 0: #알파벳이 같고 방문하지 않은 점일 때 
                visited[ni][nj] = 1
                dfs(alpha, ni, nj, cnt + 1, si, sj)
                visited[ni][nj] = 0

def game():
    for i in range(N):
        for j in range(M):
            si, sj = i, j
            visited[si][sj] = 1
            dfs(arr[i][j], i, j, 1, si, sj) #사이클 탐색 시작 알파벳, 현재 i,j , 점 개수, 시작 i,j  
            if flag: #사이클이 있다면
                return "Yes"
    
    return "No"


N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for i in range(N)]
visited = [[0] * M for i in range(N)]
flag = 0


print(game())