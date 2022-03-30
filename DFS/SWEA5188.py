#최소합
di = [1,0] #하, 우
dj = [0,1]

def dfs(i,j,total):
    global ans
    
    visited[i][j] = 1 #방문체크
    
    if total > ans: #가지치기
        return
    
    if i == N-1 and j == N-1: 
        if total < ans: #현재 정답보다 작은 값이라면
            ans = total # new 정답

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            dfs(ni,nj,total+arr[ni][nj])
            visited[ni][nj] = 0
    
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    ans = 999
    visited = [[0] * N for i in range(N)]
    dfs(0,0,arr[0][0])
    
    print(f'#{tc} {ans}')