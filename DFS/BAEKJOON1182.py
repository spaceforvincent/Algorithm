#부분수열의 합

def dfs(n, total): 
    global cnt
    
    if n == N:
        return
    
    if total + arr[n] == target:
        cnt += 1
    
    
    # n번 요소 포함안함
    dfs(n + 1, total)
    # n번 요소 포함
    dfs(n + 1, total + arr[n])
    


import sys


N, target = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
dfs(0, 0)

print(cnt)
