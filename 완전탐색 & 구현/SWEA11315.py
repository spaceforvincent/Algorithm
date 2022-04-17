# 위에서 아래로, 그리고 왼쪽에서 오른쪽으로 가면서 'o'를 찾고 있었기 때문에 굳이 왼쪽방향, 위쪽방향은 'o'를 확인할 필요가 없다.
# 우측, 아래, 우하, 좌하만 오목이 만들어지는지 확인해주면 된다. 
# arr에 오목이 존재하면 'Yes', 없으면 'No' 리턴
def check(arr):
    di = [0,1,1,1]
    dj = [1,0,1,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o': #start 지점 찾기
                for k in range(4): #4방향으로 오목이 존재하는가?
                    cnt = 0
                    ni = i
                    nj = j
                    while 0<=ni<=N-1 and 0<=nj<=N-1 and arr[ni][nj] == 'o':
                        cnt += 1
                        ni += di[k]
                        nj += dj[k]
                    if cnt ==5:
                        return 'YES'

    return 'NO'


T = int(input())
for tc in range (1,T+1):
    N = int(input()) #N x N
    arr = [input() for i in range(N)] #오목판

    print(f'#{tc} {check(arr)}')

