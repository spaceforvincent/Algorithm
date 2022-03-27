#처음에 접근했던 그리디 방식
T = int(input())

di = [1,0] #하, 우
dj = [0,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    i = 0
    j = 0
    total = arr[i][j]
    while True:
        choice = []
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                choice.append(arr[ni][nj])
        for kk in range(2):
            ni = i + di[kk]
            nj = j + dj[kk]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] == min(choice):
                    total += arr[ni][nj]
                    i = ni
                    j = nj
        if i == N-1 and j == N-1:
            break 
    print(total)

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