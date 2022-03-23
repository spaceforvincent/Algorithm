#미로

def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return [i,j] 

def dfs(i,j):
    visited[i][j] = 1
    
    if arr[i][j] == 3:
        return 1
    
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N :
            if arr[ni][nj] != 1 and visited[ni][nj] == 0 :
                if dfs(ni,nj) == 1:
                    return 1
                
    return 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]
    #좌표로 접근해야할 문제
    visited = [[0] * N for i in range(N)]
    
    print(f'#{tc} {dfs(*find_start())}')

    

