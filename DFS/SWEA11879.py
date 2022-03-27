#미로
import sys
sys.stdin = open('swea11879_input.txt')

def find_start(): #출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  
                return [i, j]

def find_3(i,j) : #3 찾기
    visited.append([i,j]) #방문처리 (좌표 기록)

    if arr[i][j] == 3: #3에 이르렀는가?
        return 1 #함수 실행위치로 1 가지고 돌아감

    for k in range(4): #4방향 탐색
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni <=N-1 and 0<= nj <= N-1:
            if arr[ni][nj] != 1 and [ni,nj] not in visited:
                if find_3(ni,nj) == 1:
                    return 1 #함수 실행 위치로 1 가지고 돌아감
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #N x N
    arr = [list(map(int, input())) for i in range(N)]
    
    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1]

    visited = []
    print(f'#{tc} {find_3(*find_start())}')
    
    