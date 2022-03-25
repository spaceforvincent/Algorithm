#사탕게임
import sys

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().rstrip()) for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(N-1):
        arr[i][j], arr[i][j+1] = arr[j+1], arr[i][j]
        
