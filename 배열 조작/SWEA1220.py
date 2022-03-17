#Magnetic
import sys
sys.stdin = open('swea1220_input.txt')
T = 10
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    cnt = 0
    for i in range(N):  #1은 빨강, 2는 파랑
        flag = 0
        for j in range(N):
            if arr[j][i] == 1:
                flag = 1
            elif arr[j][i] == 2 and flag == 1:
                cnt += 1
                flag = 0
    print(f'#{tc} {cnt}')
