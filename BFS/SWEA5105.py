#미로의 거리

def find_start(): #출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j

def bfs(v):
    Q = []
    #enQue하면서 방문체크
    Q.append(v)
    visited.append(v) 
    while Q: #Q가 비어있지 않은 동안
        v = Q.pop(0)
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]  
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and (ni,nj) not in visited: 
                Q.append((ni,nj))
                visited.append((ni,nj)) #방문기록
                cnt[ni][nj] = cnt[v[0]][v[1]] + 1
                if arr[ni][nj] == 3:
                    return cnt[ni][nj] - 1
    return 0 #3까지 가는 경로가 없을 때
                


T = int(input())
for tc in range(1,T+1):
    N = int(input()) #배열 크기
    arr = [list(map(int, list(input()))) for i in range(N)]
    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1] 
    visited = []
    cnt = [[0] * N for i in range(N)] #0 적힌 좌표 따라가면서 거리 기록 남기기
    
    print(f'#{tc} {bfs((find_start()[0],find_start()[1]))}')