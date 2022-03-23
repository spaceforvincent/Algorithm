#파리퇴치 3
import sys
sys.stdin = open('swea12712_input.txt')

T = int(input())

for tc in range(1,T+1):
    N, P= map(int,input().split()) #배열 크기, 스프레이 세기

    di = [-1,1,0,0] #상하좌우
    dj = [0,0,-1,1]
    dx = [-1,-1,1,1] #좌상, 우상, 좌하, 우하
    dy = [-1,1,-1,1]

    arr = [list(map(int,input().split())) for i in range(N)]

    maxV = 0
    #십자 모양으로 뿌릴 때
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                for a in range(1,P):
                    ni = i + di[k] * a
                    nj = j + dj[k] * a
                    if 0<=ni<N and 0<=nj<N:
                        s+= arr[ni][nj]
            if maxV < s:
                maxV = s

    #X자 모양으로 뿌릴 때
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for k in range(4):
                for a in range(1,P):
                    nx = i + dx[k] * a
                    ny = j + dy[k] * a
                    if 0<=nx<N and 0<=ny<N:
                        s+= arr[nx][ny]
            if maxV < s:
                maxV = s

    print(f'#{tc} {maxV}')