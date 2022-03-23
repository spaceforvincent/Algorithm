#subtree

def dfs(N):
    global cnt
    cnt += 1
    #방문체크
    if visited[N] == 0:
        visited[N] = 1

    for line in lst:
        if line[0] == N and visited[line[1]] == 0:
            dfs(line[1])
    
    return cnt

T = int(input())
for tc in range(1,T+1):
    E,N = map(int, input().split())
    V = list(map(int,input().split()))
    
    visited = [0] * (E+2)
    
    #인접리스트 만들기
    lst = []
    for i in range(0,len(V)-1, 2):
        lst.append([V[i],V[i+1]])
    cnt = 0
    print(f'#{tc} {dfs(N)}')