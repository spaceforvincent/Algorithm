#IM 예제 연습

import sys
sys.stdin = open('IM연습_input.txt')

d = {'A': 1, 'B' : 2, 'C' : 3}

def check(a,i,j):
    for _ in range(a):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<=ni<=N and 0<=nj<=N-1:
            i = ni
            j = nj
            if arr[ni][nj] == 'H':
                arr[ni][nj] = 'o'

#델타탐색
di = [-1,1,0,0]
dj = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #배열 크기
    arr = [list(input()) for i in range(N+1)]

    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    check(d[arr[i][j]],i,j)
            elif arr[i][j] == 'B':
                for k in range(4):
                    check(d[arr[i][j]],i,j)
            elif arr[i][j] == 'C':
                for k in range(4):
                    check(d[arr[i][j]],i,j)
                
    
    cnt = 0
    for i in range(N+1):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt+=1

    print(cnt)

