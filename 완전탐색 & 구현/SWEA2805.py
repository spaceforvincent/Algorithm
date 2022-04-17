#농작물 수확하기
import sys
sys.stdin = open('swea2805_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #배열 크기
    field = [list(map(int, list(input()))) for i in range(N)]

    di = [-1,1,1,-1,-1] #상, 좌하, 우하, 우상, 좌상
    dj = [0,-1,1,1,-1]

    income = field[N//2][N//2] #출발점 더해주고 시작

    for m in range(1,(N//2)+1):
        i = j = N//2 #출발점 재설정
        for k in range(5): #5방향 이동
            for a in range(m):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<=N-1 and 0<=nj<=N-1:
                    i = ni #ni, nj는 현재 위치가 됨
                    j = nj
                    if field[ni][nj] != 6:
                        income += field[ni][nj] #이렇게 하면 6인 곳에서는 수입을 먹지 않음
                        field[ni][nj] = 6 #방문처리
        
    print(f'#{tc} {income}')