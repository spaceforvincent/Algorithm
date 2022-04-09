#2차원 배열의 합

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

problem = int(sys.stdin.readline())

for i in range(problem):
    s1,s2,e1,e2 = map(int, sys.stdin.readline().split())

    total = 0
    for j in range(s2-1,e2):
        for k in range(s1-1,e1): 
            total += arr[k][j] 
    
    print(total)