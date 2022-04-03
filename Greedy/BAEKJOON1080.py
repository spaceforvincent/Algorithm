#행렬
def change(i,j):
        for k in range(i,i+3):
            for m in range(j,j+3):
                if arr_1[k][m] == 1:
                    arr_1[k][m] = 0
                else:
                    arr_1[k][m] = 1
                
import sys
N,M = map(int, sys.stdin.readline().split())

arr_1 = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]
arr_2 = [list(map(int, sys.stdin.readline().rstrip())) for i in range(N)]
cnt = 0

#3x3 틀을 대보면서 움직이자
for i in range(N-2):
    for j in range(M-2):
        if arr_1[i][j] != arr_2[i][j]:
            change(i,j)
            cnt += 1

if arr_1 != arr_2:
    print(-1)
else:
    print(cnt)
