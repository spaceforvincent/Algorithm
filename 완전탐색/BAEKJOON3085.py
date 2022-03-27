#사탕게임
import sys

def width_check(arr, N): #가로 체크
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[i][j] != arr[i][j+1]:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
            else:
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt

def height_check(arr, N): #세로 체크
    global max_cnt
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if arr[j][i] != arr[j+1][i]:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
            else:
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for i in range(N)]
max_cnt = 0

#가로 교환
for i in range(N):
    for j in range(N-1):
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        width_check(arr,N) 
        height_check(arr,N)
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
#세로 교환
for i in range(N):
    for j in range(N-1):
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
        width_check(arr,N) 
        height_check(arr,N)
        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

print(max_cnt)