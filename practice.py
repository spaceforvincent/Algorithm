# def run(n):
#     if n == 5:
#         return
#     print(n)
#     run(n-1)
#     print(n)

# run(10)

from collections import deque

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs():
    Q = deque()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                Q.append((i,j))
    while Q:
        i,j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<4 and 0<=nj<4 and arr[ni][nj] == 0:
                arr[ni][nj] = arr[i][j] + 1
                Q.append((ni,nj))

arr = [[0] * 4 for i in range(4)]
arr[1][1] = 1

bfs()
print(arr)